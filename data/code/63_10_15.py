def reverse_integer(n: int) -> int:
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result

if __name__ == '__main__':
    sample_value = 12345
    reversed_value = reverse_integer(sample_value)
    print(reversed_value)