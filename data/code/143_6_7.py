def preprocess(sentence):
    return sentence.lower().split()

def compare_sents(sent1, sent2):
    words1 = set(preprocess(sent1))
    words2 = set(preprocess(sent2))
    return not words1 & words2
if __name__ == '__main__':
    sent1 = 'The cat is on the mat.'
    sent2 = 'A dog is barking outside.'
    print(compare_sents(sent1, sent2))