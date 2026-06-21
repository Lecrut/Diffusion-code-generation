def evaluate_conditions(a: int, b: int, c: int) -> bool:
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("All arguments must be integers")
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    return positive_count >= 2

if __name__ == '__main__':
    result = evaluate_conditions(5, -10, 15)
    print(result)