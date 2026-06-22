def evaluate_conditions(a: int, b: int, c: int) -> bool:
    return (a > 0 and b > 0) or (c < 0 and a == b)

if __name__ == '__main__':
    result = evaluate_conditions(5, 3, -1)
    print(result)