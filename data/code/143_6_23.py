def analyze_contradictions(sentence1: str, sentence2: str) -> bool:
    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())
    return not words1.isdisjoint(words2)

if __name__ == '__main__':
    print(analyze_contradictions("I love cats", "Cats are great pets"))