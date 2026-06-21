class SentenceChecker:
    def __init__(self, sentences):
        self.word_set = set(word for sentence in sentences for word in sentence.split())

    def check_word(self, word):
        return word in self.word_set

if __name__ == '__main__':
    sample_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "A stitch in time saves nine",
        "Every cloud has a silver lining"
    ]
    checker = SentenceChecker(sample_sentences)
    
    print(f"Checking word 'quick': {checker.check_word('quick')}")
    print(f"Checking word 'zoo': {checker.check_word('zoo')}")