def analyze_semantic_contradictions(sentence1, sentence2):
    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())
    return not words1.isdisjoint(words2)

if __name__ == '__main__':
    sentence1 = "The cat is on the mat."
    sentence2 = "The dog is under the table."
    print(analyze_semantic_contradictions(sentence1, sentence2))