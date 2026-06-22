def evaluate_conditions(a: int, b: int, c: int) -> bool:
    if a > 0 and b > 0:
        return True
    if a > 0 and c > 0:
        return True
    if b > 0 and c > 0:
        return True
    return False
if __name__ == '__main__':
    result = evaluate_conditions(1, -2, 3)
    print(result)