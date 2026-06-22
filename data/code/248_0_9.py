def add_two_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    num1 = 25
    num2 = 35
    result = add_two_integers(num1, num2)
    print(result)