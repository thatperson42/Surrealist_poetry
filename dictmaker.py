# dictmaker.py

import nltk
from nltk.tag.simplify import simplify_wsj_tag

# dict_location will have to be modified depending on the system.
dict_location = "/usr/share/dict/words"

def make_wordlist():
    f = open(dict_location, 'r')
    dictionary = f.read()
    f.close()
    # Shortening the dictionary, starting around the start of the
    # lowercase letters in my unix dictionary. Otherwise the tokenize
    # takes too long. 
    dictwords = [w for w in nltk.word_tokenize(dictionary) if w != "'s" and w != "n't"]
    dictwords = dictwords[18300:]
    short_dict = []
    for i in xrange(len(dictwords)/10):
        short_dict.append(dictwords[10*i])
    words = []
    words = nltk.pos_tag(short_dict)
    
    # simplifying the part of speech of the words following advice at:
    # http://stackoverflow.com/a/5793083 here:
    simple_words = [(word, simplify_wsj_tag(tag)) for word, tag in words]
    return simple_words

# speech_lists fills in the lists of words
def speech_lists():
    for k in simple_words:
        if (k[1] == "N"):
            nouns.append(k[0])
        elif (k[1] == "V"): # only present tense verbs
            verbs.append(k[0])
        elif (k[1] == "ADJ"):
            adjectives.append(k[0])
        elif (k[1] == "ADV"):
            adverbs.append(k[0])
        else:
            pass
    return


# First we make the list of words:
simple_words = make_wordlist()

# Now we make the lists of different types of words:
# simplified parts-of-speech are available at Table 5.1 at:
# http://nltk.googlecode.com/svn/trunk/doc/book/ch05.html#tab-simplified-tagset
verbs = []
adjectives = []
adverbs = []
nouns = []

speech_lists()

"""
Now we write the words to the file in the following order:

adj
noun
verb
adv
prep
conj
punc
art
sim
"""
g = open("poetry_wordlist2", 'w')
g.write("<adj>\n")
for k in adjectives:
    g.write(k+"\n")
g.write("</adj>\n")
g.write("<noun>\n")
for k in nouns:
    g.write(k+"\n")
g.write("</noun>\n")
g.write("<verb>\n")
for k in verbs:
    g.write(k+"\n")
g.write("</verb>\n")
g.write("<adv>\n")
for k in adverbs:
    g.write(k+"\n")
g.write("</adv>\n")

# The end is from Matt's dictionary. I thought adding more things here
# could mess up the poem because lots of things could happen
# grammatically.
g.write("""
<prep>
towards
beneath
in
on
through
by
at
around
with
for
after
</prep>

<conj>
and
but
since
then
</conj>

<punc>
.
,
!
?
:
;
</punc>

<art>
the
a
</art>

<sim>
like
as
</sim>""")
