class WordReverser:
    @staticmethod
    def reverse_words(text):
        words = text.split()
        words.reverse()
        return " ".join(words)

if __name__ == '__main__':
    sample_string1 = "hello world this is a test"
    result1 = WordReverser.reverse_words(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: '{result1}'")

    sample_string2 = "optimization is key"
    result2 = WordReverser.reverse_words(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Output: '{result2}'")

    sample_string3 = "  leading and trailing spaces   "
    result3 = WordReverser.reverse_words(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: '{result3}'")