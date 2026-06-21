def preprocess(sentence):
    return sentence.lower().split()

def find_contradictions(sentence1, sentence2):
    words1 = set(preprocess(sentence1))
    words2 = set(preprocess(sentence2))
    contradictions = words1.symmetric_difference(words2)
    return contradictions

if __name__ == '__main__':
    sentence1 = "The sky is blue."
    sentence2 = "The sun is bright."
    print(find_contradictions(sentence1, sentence2))