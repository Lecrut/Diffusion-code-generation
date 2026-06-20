def evaluate_conditions(a: int, b: int, c: int) -> bool:
    return sum(x > 0 for x in (a, b, c)) >= 2

if __name__ == '__main__':
    print(evaluate_conditions(1, -2, 3))
    print(evaluate_conditions(-1, -2, -3))
    print(evaluate_conditions(0, 0, 0))