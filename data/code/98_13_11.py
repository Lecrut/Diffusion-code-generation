def evaluate_conditions(a: int, b: int, c: int) -> bool:
    conditions = {
        'a': a > 0,
        'b': b > 0,
        'c': c > 0,
    }
    return sum(conditions.values()) >= 2

if __name__ == '__main__':
    result = evaluate_conditions(1, -2, 3)
    print(result)