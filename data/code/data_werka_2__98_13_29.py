def evaluate_conditions(a: int, b: int, c: int) -> bool:
    positive_count = (a > 0) + (b > 0) + (c > 0)
    return positive_count >= 2

if __name__ == '__main__':
    result = evaluate_conditions(5, -10, 15)
    print(result)