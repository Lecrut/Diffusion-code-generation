def reverse_integer(n: int) -> int:
    if n == 0:
        return 0
    
    negative = n < 0
    val = -n if negative else n
    
    reversed_val = 0
    while val > 0:
        digit = val % 10
        reversed_val = reversed_val * 10 + digit
        val //= 10
    
    return -reversed_val if negative else reversed_val

if __name__ == '__main__':
    result1 = reverse_integer(123)
    print(result1)
    
    result2 = reverse_integer(-456)
    print(result2)
    
    result3 = reverse_integer(1200)
    print(result3)