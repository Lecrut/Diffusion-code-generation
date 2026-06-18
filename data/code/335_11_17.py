import re
class SentenceProcessor:
    def split_words(self, sentence):
        return [word for word in re.split(r'\s+', sentence) if len(word.strip()) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentence = "Hello   world! This is a test."
    result = processor.split_words(sample_sentence)
    print(result)