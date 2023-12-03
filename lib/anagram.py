# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        anagrams = []

        for candidate in words:
            if self.is_anagram(candidate):
                anagrams.append(candidate)

        return anagrams

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()

        return candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word)
