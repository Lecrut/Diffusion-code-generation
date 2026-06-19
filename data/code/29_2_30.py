class StringReverser:
    def reverse(self, word):
        reversed_word = ''
        for char in word:
            reversed_word = char + reversed_word
        return reversed_word

if __name__ == '__main__':
    reverser = StringReverser()
    sample_input = "Alibaba Cloud"
    result = reverser.reverse(sample_input)
    print(f"Original: {sample_input}, Reversed: {result}")