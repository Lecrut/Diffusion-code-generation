def reverse_integer(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

if __name__ == '__main__':
    sample_values = [123, 4567, 987654321, 100]
    for val in sample_values:
        result = reverse_integer(val)
        print(result)