def analyze_contradictions(sentence1, sentence2):
    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())
    
    contradictions = words1.intersection(words2)
    
    return contradictions

if __name__ == '__main__':
    sentence1 = "The sky is blue."
    sentence2 = "The grass is green."
    print(analyze_contradictions(sentence1, sentence2))