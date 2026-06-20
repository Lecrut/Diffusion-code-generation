DIVISOR = 2

def divide_pairs(pairs):
    for num1, num2 in pairs:
        if num2 == DIVISOR:
            yield num1 / num2

if __name__ == '__main__':
    sample_pairs = [(4, 2), (9, 3), (10, 5)]
    for result in divide_pairs(sample_pairs):
        print(result)