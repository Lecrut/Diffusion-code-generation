def check_values(a, b, c):
    is_positive = a > 0
    is_even = b % 2 == 0
    is_divisible = a != 0 and c % a == 0
    return (is_positive, is_even, is_divisible)

if __name__ == '__main__':
    result = check_values(5, 4, 10)
    print(result)