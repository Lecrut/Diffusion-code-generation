class StringReverser:
    def reverse(self, word):
        return ''.join(reversed(word))

if __name__ == '__main__':
    reverser = StringReverser()
    SAMPLE_WORD_1 = "hello"
    SAMPLE_WORD_2 = "world"
    SAMPLE_WORD_3 = "Python"
    
    print(f"Original: {SAMPLE_WORD_1}, Reversed: {reverser.reverse(SAMPLE_WORD_1)}")
    print(f"Original: {SAMPLE_WORD_2}, Reversed: {reverser.reverse(SAMPLE_WORD_2)}")
    print(f"Original: {SAMPLE_WORD_3}, Reversed: {reverser.reverse(SAMPLE_WORD_3)}")