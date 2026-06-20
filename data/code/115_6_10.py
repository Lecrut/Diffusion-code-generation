DIVISOR_THRESHOLD = 1e-10

def divide_pairs(pairs):
    for num1, num2 in pairs:
        if abs(num2) < DIVISOR_THRESHOLD:
            raise ValueError("Division by near-zero is not allowed")
        yield num1 / num2

if __name__ == '__main__':
    sample_pairs = [(4, 2), (9, 3), (10, 5)]
    for result in divide_pairs(sample_pairs):
        print(result)