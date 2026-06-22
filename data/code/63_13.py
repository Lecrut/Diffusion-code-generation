def reverse_integer(n: int) -> int:
    negative = n < 0
    x = abs(n)
    reversed_val = 0
    while x > 0:
        digit = x % 10
        reversed_val = reversed_val * 10 + digit
        x //= 10
    return -reversed_val if negative else reversed_val

if __name__ == '__main__':
    sample_values = [123, -456, 1200, 0, -7890]
    for value in sample_values:
        print(reverse_integer(value))