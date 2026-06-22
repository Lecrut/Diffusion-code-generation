class WordCounter:
    @staticmethod
    def count_words(sentence):
        word_count = {}
        words = sentence.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

if __name__ == '__main__':
    sample_sentence = "hello world hello"
    result = WordCounter.count_words(sample_sentence)
    print(result)