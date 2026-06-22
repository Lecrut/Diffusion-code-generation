class WordCounter:
    def count_words(self, text):
        if not text:
            return 0
        words = text.split()
        return len(words)

if __name__ == '__main__':
    counter = WordCounter()
    sample_string1 = "This is a test sentence with multiple spaces."
    sample_string2 = "  leading and trailing spaces   \tand newlines\n"
    sample_string3 = ""
    sample_string4 = "OneWord"
    sample_string5 = "word1  word2\tword3"
    
    print(f"'{sample_string1}': {counter.count_words(sample_string1)}")
    print(f"'{sample_string2}': {counter.count_words(sample_string2)}")
    print(f"'{sample_string3}': {counter.count_words(sample_string3)}")
    print(f"'{sample_string4}': {counter.count_words(sample_string4)}")
    print(f"'{sample_string5}': {counter.count_words(sample_string5)}")