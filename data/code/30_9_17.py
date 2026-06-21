def decimal_to_binary_string(n):
    if n == 0:
        return "0"
    
    negative = False
    if n < 0:
        negative = True
        n = -n
    
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    
    if negative:
        return "-" + "".join(reversed(binary_digits))
    else:
        return "".join(reversed(binary_digits))

if __name__ == '__main__':
    print(decimal_to_binary_string(0))
    print(decimal_to_binary_string(1))
    print(decimal_to_binary_string(2))
    print(decimal_to_binary_string(5))
    print(decimal_to_binary_string(10))
    print(decimal_to_binary_string(255))
    print(decimal_to_binary_string(-42))