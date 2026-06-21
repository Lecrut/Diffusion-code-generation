def int_to_binary(n):
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n // 2
    
    return result

if __name__ == '__main__':
    print(int_to_binary(0))
    print(int_to_binary(1))
    print(int_to_binary(10))
    print(int_to_binary(255))