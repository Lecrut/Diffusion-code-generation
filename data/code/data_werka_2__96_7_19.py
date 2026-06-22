import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def main():
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    result = evaluate_expression(sample_a, sample_b, sample_c, sample_d)
    print(result)

    for _ in range(100):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        expected = (a and b) or (c and not d)
        actual = evaluate_expression(a, b, c, d)
        if expected != actual:
            raise AssertionError(f"Mismatch for {a}, {b}, {c}, {d}")

if __name__ == '__main__':
    main()