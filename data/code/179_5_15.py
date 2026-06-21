class StringReverser:
    @staticmethod
    def reverse_words(text: str) -> str:
        words = text.split()
        words.reverse()
        return " ".join(words)

if __name__ == '__main__':
    sample_string = "Python is awesome"
    reversed_string = StringReverser.reverse_words(sample_string)
    print(f"'{sample_string}' -> '{reversed_string}'")