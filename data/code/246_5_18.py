def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    print(add_numbers(10, 5))
    print(add_numbers(12.5, 3.5))
    print(add_numbers("hello", 5))
    print(add_numbers(7, "invalid"))
    print(add_numbers("", 10))