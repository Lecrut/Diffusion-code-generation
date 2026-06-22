class WordReverser:
    def __init__(self):
        self.reverse_map = {
            'hello': 'olleh',
            'world': 'dlrow',
            'Python': 'nohtyP',
            'racecar': 'racecar'
        }

    def reverse_word(self, word):
        if word in self.reverse_map:
            return self.reverse_map[word]
        else:
            return word[::-1]

if __name__ == '__main__':
    reverser = WordReverser()
    sample_words = ["hello", "world", "Python", "racecar", "example"]
    for word in sample_words:
        reversed_word = reverser.reverse_word(word)
        print(f"Original: {word}, Reversed: {reversed_word}")