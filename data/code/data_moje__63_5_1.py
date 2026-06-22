def reverse_integer(x):
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    
    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    reversed_num *= sign
    
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(1534236469))