def reverse_integer(n):
    if n < 0:
        sign = -1
        abs_str = str(-n)
    else:
        sign = 1
        abs_str = str(n)
    
    reversed_str = abs_str[::-1]
    return sign * int(reversed_str)

if __name__ == '__main__':
    test_cases = [123, -456, 0, 1200, -98765, 1000000003]
    for num in test_cases:
        result = reverse_integer(num)
        print(result)