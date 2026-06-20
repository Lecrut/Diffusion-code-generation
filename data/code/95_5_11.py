def check_values(a, b, c):
    is_positive = a > 0
    is_even = b % 2 == 0
    is_divisible = c % a == 0 if a != 0 else False
    return (is_positive, is_even, is_divisible)

if __name__ == '__main__':
    result = check_values(5, 4, 10)
    print(result)