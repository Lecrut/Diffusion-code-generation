def is_negative(number):
    return number < 0

if __name__ == '__main__':
    num1 = -23
    num2 = 456
    result1 = is_negative(num1)
    result2 = is_negative(num2)
    print(f"is_negative({num1}): {result1}")
    print(f"is_negative({num2}): {result2}")