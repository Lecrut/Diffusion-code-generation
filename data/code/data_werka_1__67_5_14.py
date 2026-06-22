def add_numbers(a, b):
    try:
        result = a + b
    except TypeError:
        return 'Error: Both inputs must be numbers.'
    return result
if __name__ == '__main__':
    print(add_numbers(5, 10))
    print(add_numbers('5', 10))
    print(add_numbers(3.5, 2.5))