def is_even(n):
    remainder = n % 2
    return remainder == 0

if __name__ == '__main__':
    number = 42
    result = is_even(number)
    print(result)
    number = 53
    result = is_even(number)
    print(result)
    number = 0
    result = is_even(number)
    print(result)
    number = -11
    result = is_even(number)
    print(result)