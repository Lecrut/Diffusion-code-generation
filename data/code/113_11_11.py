MAX_INT = 2147483647

def subtract_large_integers(a: int, b: int) -> int:
    return a - b if a >= b else MAX_INT + (a - b)

if __name__ == '__main__':
    num1 = 2000000000
    num2 = 1500000000
    result = subtract_large_integers(num1, num2)
    print(result)