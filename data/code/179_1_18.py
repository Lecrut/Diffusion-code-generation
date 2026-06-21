class WordReverser:
    def reverse(self, text):
        words = text.split()
        words.reverse()
        return " ".join(words)

if __name__ == '__main__':
    reverser = WordReverser()
    test_string1 = "Hello World from Python"
    print(f"Input: '{test_string1}'")
    print(f"Output: '{reverser.reverse(test_string1)}'")