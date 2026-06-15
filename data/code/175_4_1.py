class StringProcessor:
    @staticmethod
    def process_sentence(sentence):
        words = sentence.split()
        result = {}
        for index, word in enumerate(words):
            result[word] = index
        return result
if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for testing"
    word_indices = StringProcessor.process_sentence(sample_sentence)
    print(word_indices)