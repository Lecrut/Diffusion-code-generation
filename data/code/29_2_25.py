class StringReverser:
    def reverse(self, word):
        reversed_word = ''
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word

if __name__ == '__main__':
    reverser = StringReverser()
    sample_words = ["hello", "world", "Python"]
    for word in sample_words:
        print(f"Original: {word}, Reversed: {reverser.reverse(word)}")