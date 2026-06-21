def greater_of_two(a, b):
    def is_integer(x):
        return isinstance(x, int)

    if not (is_integer(a) and is_integer(b)):
        raise ValueError('Both inputs must be integers')

    return (a + b + abs(a - b)) // 2

if __name__ == '__main__':
    num1 = 100
    num2 = 50
    result = greater_of_two(num1, num2)
    print(result)