class WordReverser:
    def reverse_word_order(self, s):
        words = s.split()
        return " ".join(reversed(words))

if __name__ == '__main__':
    reverser = WordReverser()
    sample_string1 = "Data Science is fun"
    result1 = reverser.reverse_word_order(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: '{result1}'")