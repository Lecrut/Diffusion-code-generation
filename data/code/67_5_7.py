def add_numbers(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Both inputs must be numbers."

if __name__ == '__main__':
    print(add_numbers(10, 20))
    print(add_numbers(30.5, 40.5))
    print(add_numbers("hello", 5))
    print(add_numbers([1, 2], [3, 4]))