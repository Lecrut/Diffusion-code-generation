def evaluate_contradiction(str1: str, str2: str) -> bool:
    set1 = set(word.lower() for word in str1.split())
    set2 = set(word.lower() for word in str2.split())
    return not set1.intersection(set2)

if __name__ == '__main__':
    print(evaluate_contradiction("apple orange", "banana apple"))
    print(evaluate_contradiction("red blue", "green yellow"))