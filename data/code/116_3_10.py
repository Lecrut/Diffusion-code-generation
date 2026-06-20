def sum_three_numbers(a, b, c):
    return a + b + c

if __name__ == '__main__':
    numbers = {'a': 10, 'b': 20, 'c': 30}
    result = sum_three_numbers(numbers['a'], numbers['b'], numbers['c'])
    print(result)