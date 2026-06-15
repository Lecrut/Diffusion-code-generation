class StringProcessor:
    @staticmethod
    def process_string(text):
        words = text.split()
        result = {}
        for index, word in enumerate(words):
            result[word] = index
        return result
if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for testing purposes"
    word_indices = StringProcessor.process_string(sample_sentence)
    print(word_indices)