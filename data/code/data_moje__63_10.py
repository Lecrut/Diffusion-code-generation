def reverse_integer(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

if __name__ == '__main__':
    sample_values = [123, 405, 9876, 5]
    for value in sample_values:
        print(reverse_integer(value))