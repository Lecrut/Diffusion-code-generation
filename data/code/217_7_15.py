def subtract_without_arithmetic(a: int, b: int) -> int:
    while b != 0:
        borrow = (~a) & b
        a ^= b
        b = borrow << 1
    return a

def is_greater(a: int, b: int) -> bool:
    if a < 0 and b >= 0:
        return False
    elif a >= 0 and b < 0:
        return True
    else:
        return subtract_without_arithmetic(a, b) == a

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = is_greater(num1, num2)
    print(f"Is {num1} greater than {num2}? {result1}")
    
    num3 = 7
    num4 = 7
    result2 = is_greater(num3, num4)
    print(f"Is {num3} greater than {num4}? {result2}")
    
    num5 = 20
    num6 = 15
    result3 = is_greater(num5, num6)
    print(f"Is {num5} greater than {num6}? {result3}")