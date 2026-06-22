def reverse_digits(n):
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    return reversed_n

if __name__ == '__main__':
    sample_values = [123, 4567, 900, 1]
    for val in sample_values:
        print(reverse_digits(val))