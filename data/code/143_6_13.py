def preprocess(sentence):
    return set(word.lower() for word in sentence.split())

def compare_sentences(sent1, sent2):
    words1 = preprocess(sent1)
    words2 = preprocess(sent2)
    return not words1 & words2

if __name__ == '__main__':
    sentence1 = "I love Python programming."
    sentence2 = "Python is a great language for data analysis."
    print(compare_sentences(sentence1, sentence2))