POSITIVE_THRESHOLD = 0

def check_conditions(a, b, c):
    is_positive = a > POSITIVE_THRESHOLD
    is_even = b % 2 == 0
    is_divisible = c % a == 0
    return (is_positive, is_even, is_divisible)

if __name__ == '__main__':
    result = check_conditions(10, 12, 30)
    print(result)