def reverse_binary(n):
    if n < 0:
        return "Negative numbers are not supported"
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n // 2
    
    return result

if __name__ == '__main__':
    num = 26
    binary_str = reverse_binary(num)
    print(binary_str)