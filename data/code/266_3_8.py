class WordProcessor:
    @staticmethod
    def find_longest_word(words):
        longest_word = ""
        max_length = 0
        for word in words:
            if len(word) > max_length:
                longest_word = word
                max_length = len(word)
        return longest_word, max_length

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    processor = WordProcessor()
    result = processor.find_longest_word(sample_words)
    print(f"Longest word: {result[0]}, Length: {result[1]}")