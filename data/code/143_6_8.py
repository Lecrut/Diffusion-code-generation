def preprocess(sentence):
    return sentence.lower().replace('.', '').split()

def compare_sentences(sent1, sent2):
    words1 = set(preprocess(sent1))
    words2 = set(preprocess(sent2))
    return not words1 & words2
if __name__ == '__main__':
    sentence1 = 'The sky is blue.'
    sentence2 = 'The grass is green.'
    print(compare_sentences(sentence1, sentence2))