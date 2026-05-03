def is_strictly_greater(a, b):
    try:
        return a > b
    except TypeError:
        return False
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = is_strictly_greater(num1, num2)
    print(f"Is {num1} strictly greater than {num2}? {result1}")
    num3 = 3
    num4 = 7
    result2 = is_strictly_greater(num3, num4)
    print(f"Is {num3} strictly greater than {num4}? {result2}")
    num5 = 10
    num6 = 10
    result3 = is_strictly_greater(num5, num6)
    print(f"Is {num5} strictly greater than {num6}? {result3}")
    num7 = "a"
    num8 = 5
    result4 = is_strictly_greater(num7, num8)
    print(f"Is {num7} strictly greater than {num8}? {result4}")