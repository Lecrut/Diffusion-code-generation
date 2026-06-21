class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_input = "This is a sample sentence"
    result = reverser.reverse_words(sample_input)
    print(result)