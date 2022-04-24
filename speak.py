#!/usr/bin/env python

from string import ascii_lowercase
from english_words import english_words_lower_alpha_set as words


hexspeak_tr = {
	'a': 'A',
	'b': 'B',
	'c': 'C',
	'd': 'D',
	'e': 'E',
	'f': 'F',
	'g': '6',
	'i': '1',
	'l': '1',
	'o': '0',
	's': '5',
	't': '7',
}

unavailable = set(ascii_lowercase).difference(hexspeak_tr.keys())

length = 8


def tohexspeak(word):
	return word.translate(word.maketrans(hexspeak_tr))


def istranslatable(word):
	return len(word) == length and not unavailable.intersection(word)


filtered = filter(istranslatable, words)

for word in filtered:
	print(tohexspeak(word))
