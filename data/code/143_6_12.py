def preprocess(sentence):
    return set(sentence.lower().split())

def compare_sents(sent1, sent2):
    words1 = preprocess(sent1)
    words2 = preprocess(sent2)
    return not words1.intersection(words2)
if __name__ == '__main__':
    sentence1 = 'I love Python programming.'
    sentence2 = 'Python is a great language for data analysis.'
    print(compare_sents(sentence1, sentence2))