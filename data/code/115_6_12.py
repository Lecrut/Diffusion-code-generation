def divide_pairs(pairs):
    for num1, num2 in pairs:
        if num2 == 0:
            continue
        yield num1 / num2

if __name__ == '__main__':
    sample_pairs = [(4, 2), (9, 3), (0, 5)]
    for result in divide_pairs(sample_pairs):
        print(result)