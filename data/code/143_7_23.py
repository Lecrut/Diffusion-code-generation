def evaluate_contradiction(str1, str2):
    terms1 = set(word.lower() for word in str1.split())
    terms2 = set(word.lower() for word in str2.split())
    return not terms1.intersection(terms2)

if __name__ == '__main__':
    print(evaluate_contradiction("apple banana", "orange grape"))
    print(evaluate_contradiction("red blue", "green yellow"))
    print(evaluate_contradiction("sun moon", "moon sun"))