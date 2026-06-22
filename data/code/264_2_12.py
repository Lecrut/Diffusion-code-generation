class TextProcessor:
    def extract_distinct_words(self, text):
        cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
        words = cleaned_text.split()
        distinct_words = sorted(set(words))
        return distinct_words

if __name__ == '__main__':
    processor = TextProcessor()
    sample_text = "Hello world! This is a test, how are you doing today? Hello Python."
    distinct_word_list = processor.extract_distinct_words(sample_text)
    print(distinct_word_list)