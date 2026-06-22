def verify_values(first, second, third):
    is_positive = first > 0
    is_even = second % 2 == 0
    product = first * second
    is_divisible = third % product == 0
    return is_positive and is_even and is_divisible

if __name__ == '__main__':
    a = 3
    b = 6
    c = 18
    outcome = verify_values(a, b, c)
    print(outcome)