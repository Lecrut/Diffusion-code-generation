def add_integers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    sample_values = {'a': 3, 'b': 5}
    result = add_integers(sample_values['a'], sample_values['b'])
    print(result)