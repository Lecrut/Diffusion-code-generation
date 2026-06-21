class StringReverser:
    def reverse_word_order(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    reverser = StringReverser()
    sample_string = "Data Science is fun"
    result = reverser.reverse_word_order(sample_string)
    print(result)