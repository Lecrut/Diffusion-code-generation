def greater_of_two(a, b):
    try:
        return (a + b + ((a - b) ** 2) ** 0.5) // 2
    except TypeError:
        raise ValueError('Both inputs must be integers')
if __name__ == '__main__':
    num1 = 30
    num2 = 45
    result = greater_of_two(num1, num2)
    print(result)