def check_conditions(a: float, b: float, c: float) -> bool:
    return a > 0 and b < a and c == a + b

if __name__ == '__main__':
    sample_values = {
        'a': 5.0,
        'b': 2.0,
        'c': 7.0
    }
    print(check_conditions(**sample_values))