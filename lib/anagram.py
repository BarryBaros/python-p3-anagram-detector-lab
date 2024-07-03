# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = []
        sorted_word = sorted(self.word.lower())  # Ensure case insensitivity
        
        for word in word_list:
            if sorted_word == sorted(word.lower()):
                anagrams.append(word)
                
        return anagrams

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))

mars = Anagram("mars")
print(mars.match(['mart', 'arms', 'rams']))
