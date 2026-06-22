def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    negative = False
    if n < 0:
        negative = True
        n = -n
    
    if n == 0:
        bits = "0"
    else:
        bits = ""
        while n > 0:
            bits = str(n & 1) + bits
            n >>= 1
    
    if negative:
        return "-" + bits
    
    return bits

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-5))
    print(decimal_to_binary(255))
    print(decimal_to_binary(1024))