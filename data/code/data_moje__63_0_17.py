def reverse(x: int) -> int:
    sign = 1 if x >= 0 else -1
    abs_x = abs(x)
    reversed_str = str(abs_x)[::-1]
    reversed_val = sign * int(reversed_str)
    
    if reversed_val < -2**31 or reversed_val > 2**31 - 1:
        return 0
    return reversed_val

if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))
    print(reverse(0))
    print(reverse(1534236469))