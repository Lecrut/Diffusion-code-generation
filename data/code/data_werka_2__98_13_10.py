def evaluate_conditions(a: int, b: int, c: int) -> bool:
    count = 0
    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1
    return count >= 2

if __name__ == '__main__':
    result = evaluate_conditions(1, -2, 3)
    print(result)