def reverse_integer(n: int) -> int:
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

if __name__ == '__main__':
    sample_value = 12345
    result = reverse_integer(sample_value)
    print(result)
    sample_value_2 = 987654321
    result_2 = reverse_integer(sample_value_2)
    print(result_2)
    sample_value_3 = 100
    result_3 = reverse_integer(sample_value_3)
    print(result_3)