class TextProcessor:
    @staticmethod
    def clean_text(text):
        return ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)

    @staticmethod
    def get_distinct_words(text):
        cleaned_text = TextProcessor.clean_text(text)
        words = cleaned_text.split()
        distinct_words = sorted(set(words))
        return distinct_words

if __name__ == '__main__':
    sample_text = "Hello world! This is a test, how are you doing today?"
    processor = TextProcessor()
    word_list = processor.get_distinct_words(sample_text)
    print(word_list)