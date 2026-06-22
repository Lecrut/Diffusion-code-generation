class StringReverser:
    @staticmethod
    def reverse_words(s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)

if __name__ == '__main__':
    reverser = StringReverser()
    test_string = "hello world from python"
    result = reverser.reverse_words(test_string)
    print(result)