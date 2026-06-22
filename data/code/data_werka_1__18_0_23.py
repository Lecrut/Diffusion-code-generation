def is_strictly_greater(num1, num2):
    try:
        return float(num1) > float(num2)
    except ValueError:
        return False
if __name__ == '__main__':
    print(is_strictly_greater(5, 3))
    print(is_strictly_greater(3.5, 4.2))
    print(is_strictly_greater('10', '5'))
    print(is_strictly_greater('abc', 1))
    print(is_strictly_greater(7, 7))