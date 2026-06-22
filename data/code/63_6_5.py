def reverse_integer(n: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if n == 0:
        return 0
        
    negative = n < 0
    abs_n = abs(n)
    
    reversed_str = str(abs_n)[::-1]
    reversed_int = int(reversed_str)
    
    if negative:
        reversed_int = -reversed_int
        
    if reversed_int < INT_MIN or reversed_int > INT_MAX:
        return 0
        
    return reversed_int

if __name__ == '__main__':
    result1 = reverse_integer(123)
    print(result1)
    
    result2 = reverse_integer(-123)
    print(result2)
    
    result3 = reverse_integer(120)
    print(result3)
    
    result4 = reverse_integer(1534236469)
    print(result4)