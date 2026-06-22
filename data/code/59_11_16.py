def digit_sum(number):
    if number < 0:
        number = -number
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

if __name__ == '__main__':
    print(digit_sum(123456789012345678))
    print(digit_sum(999999999999999999))
    print(digit_sum(0))
    print(digit_sum(42))