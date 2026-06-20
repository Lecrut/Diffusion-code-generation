def sum_three(a: int, b: int, c: int) -> int:
    return a + b + c

if __name__ == '__main__':
    values = {'a': 10, 'b': 20, 'c': 30}
    result = sum_three(values['a'], values['b'], values['c'])
    print(result)