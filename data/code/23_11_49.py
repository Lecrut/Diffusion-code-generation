def greater_of_two(a, b):
    try:
        return (a + b - abs(a - b)) // 2
    except TypeError:
        raise ValueError('Both inputs must be integers')

if __name__ == '__main__':
    num1 = 75
    num2 = 48
    result = greater_of_two(num1, num2)
    print(result)