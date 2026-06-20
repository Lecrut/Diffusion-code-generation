def sum_three(a: int, b: int, c: int) -> int:
    return a + b + c

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 20,
        'c': 30
    }
    result = sum_three(sample_values['a'], sample_values['b'], sample_values['c'])
    print(result)