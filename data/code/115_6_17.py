def divide_pairs(pairs):
    for num1, num2 in pairs:
        yield num1 / num2

if __name__ == '__main__':
    sample_pairs = [(6, 3), (8, 4), (15, 5)]
    for result in divide_pairs(sample_pairs):
        print(result)