def is_larger(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError('Both arguments must be numbers')
    return num1 > num2
if __name__ == '__main__':
    try:
        print(is_larger(10, 5))
        print(is_larger(3, 7))
        print(is_larger(-1, -2))
        print(is_larger(0, 0))
        print(is_larger(5.5, 2))
        print(is_larger('a', 2))
    except ValueError as e:
        print(e)