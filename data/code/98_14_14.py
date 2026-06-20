def evaluate_conditions(a: int, b: int, c: int) -> bool:
    positive_count = sum(x > 0 for x in (a, b, c))
    return positive_count >= 2

if __name__ == '__main__':
    sample_values = [
        (-1, 2, 3),
        (4, -5, 6),
        (-7, -8, -9),
        (10, 11, 12)
    ]
    for values in sample_values:
        print(evaluate_conditions(*values))