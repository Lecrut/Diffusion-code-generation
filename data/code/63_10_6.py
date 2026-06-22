def reverse_digits(n: int) -> int:
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

if __name__ == '__main__':
    sample_input = 12345
    result = reverse_digits(sample_input)
    print(result)