def evaluate_contradiction(str1, str2):
    terms1 = set((word.lower() for word in str1.split()))
    terms2 = set((word.lower() for word in str2.split()))
    return not terms1.isdisjoint(terms2)
if __name__ == '__main__':
    print(evaluate_contradiction('apple orange', 'banana apple'))
    print(evaluate_contradiction('hello world', 'goodbye moon'))