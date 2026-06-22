def reverse_digits(n: int) -> int:
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

if __name__ == '__main__':
    sample_values = [123, 4567, 90, 1000, 8]
    for value in sample_values:
        print(reverse_digits(value))