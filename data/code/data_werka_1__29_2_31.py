class StringReverser:
    def reverse(self, word):
        return ''.join(reversed(word))

if __name__ == '__main__':
    reverser = StringReverser()
    sample_word1 = "example"
    reversed_word1 = reverser.reverse(sample_word1)
    print(f"Original: {sample_word1}, Reversed: {reversed_word1}")
    
    sample_word2 = "test"
    reversed_word2 = reverser.reverse(sample_word2)
    print(f"Original: {sample_word2}, Reversed: {reversed_word2}")
    
    sample_word3 = "Python3.8"
    reversed_word3 = reverser.reverse(sample_word3)
    print(f"Original: {sample_word3}, Reversed: {reversed_word3}")