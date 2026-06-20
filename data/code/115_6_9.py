def divide_pairs(pairs):
    for a, b in pairs:
        yield a / b

if __name__ == '__main__':
    sample_pairs = [(4, 2), (9, 3), (16, 4)]
    results = list(divide_pairs(sample_pairs))
    print(results)