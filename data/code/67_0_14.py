def sum_two_numbers(a, b):
    return a + b

if __name__ == '__main__':
    numbers = {'first': 5, 'second': 10}
    result = sum_two_numbers(numbers['first'], numbers['second'])
    print(result)