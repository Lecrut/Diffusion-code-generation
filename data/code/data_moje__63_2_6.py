def reverse_integer(n: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if n == 0:
        return 0
    
    is_negative = n < 0
    n_abs = -n if is_negative else n
    
    reversed_str = str(n_abs)[::-1]
    reversed_int = int(reversed_str)
    
    if is_negative:
        reversed_int = -reversed_int
    
    if reversed_int < INT_MIN or reversed_int > INT_MAX:
        return 0
    
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(120))
    print(reverse_integer(1534236469))