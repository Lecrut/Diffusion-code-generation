def evaluate_conditions(a: int, b: int, c: int) -> bool:
    positive_values = [val for val in (a, b, c) if val > 0]
    return len(positive_values) >= 2

if __name__ == '__main__':
    result = evaluate_conditions(10, -5, 0)
    print(result)