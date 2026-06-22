def add_numbers(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Both inputs must be numbers."

if __name__ == '__main__':
    print(add_numbers(5, 10))
    print(add_numbers(20, 'a'))
    print(add_numbers(3.5, 4.5))
    print(add_numbers('hello', 'world'))