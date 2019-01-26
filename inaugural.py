import nltk
from nltk.corpus import inaugural, stopwords
from nltk import sent_tokenize, word_tokenize
from nltk.stem import *
import pprint

# initialize pprint
pp = pprint.PrettyPrinter(indent=4)

# list of all speeches
ids = inaugural.fileids()

data = '1789-Washington.txt'

# get speech of particular file
speech = inaugural.raw(data)
speech = speech.lower()

# get sentences
sentences = inaugural.sents(data)

# sentence tokenize
sent_tokens = sent_tokenize(speech)

# print sentence
#pp.pprint(sent_tokens)

# word tokenize
word_tokens = word_tokenize(speech)

# print words
#pp.pprint(word_tokens)

stop_words = set(stopwords.words('english'))
#pp.pprint(stop_words)

# remove stop words from speech
filtered_sentence = [w for w in word_tokens if not w in stop_words]

'''
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
'''

pp.pprint(filtered_sentence)


# initialize stemmer
stemmer = PorterStemmer()

stemmed_words = []
for word in filtered_sentence:
    stemmed = stemmer.stem(word)
    stemmed_words.append(stemmed)

pp.pprint(stemmed_words)



