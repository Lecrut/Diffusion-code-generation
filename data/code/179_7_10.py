class StringReverser:
    INPUT_STRING = "Data Science is fun"

    @staticmethod
    def reverse_word_order(s):
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

if __name__ == '__main__':
    result = StringReverser.reverse_word_order(StringReverser.INPUT_STRING)
    print(result)