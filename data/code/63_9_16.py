def reverse_integer(n: int) -> int:
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    
    return sign * reversed_n

if __name__ == '__main__':
    test_cases = [123, -456, 120, 0, 1000000003]
    for num in test_cases:
        result = reverse_integer(num)
        print(result)