def evaluate_conditions(a, b, c):
    if not all((isinstance(x, int) for x in [a, b, c])):
        raise ValueError('All arguments must be integers.')
    positive_count = sum((1 for num in [a, b, c] if num > 0))
    return positive_count >= 2
if __name__ == '__main__':
    result = evaluate_conditions(1, -2, 3)
    print(result)