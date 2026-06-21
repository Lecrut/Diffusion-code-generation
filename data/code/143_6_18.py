def preprocess(sentence):
    return sentence.lower().replace('.', '').split()

def has_semantic_contradiction(sentence1, sentence2):
    words1 = set(preprocess(sentence1))
    words2 = set(preprocess(sentence2))
    return not words1.isdisjoint(words2)

if __name__ == '__main__':
    sentence1 = "The cat is on the mat."
    sentence2 = "The dog is under the table."
    print(has_semantic_contradiction(sentence1, sentence2))