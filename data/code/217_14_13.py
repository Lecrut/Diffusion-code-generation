def compare_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    
    if a < b:
        return f"{a} is less than {b}"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{a} is equal to {b}"

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    print(compare_integers(num1, num2))
    
    num3 = -3
    num4 = 7
    print(compare_integers(num3, num4))
    
    num5 = 42
    num6 = 42
    print(compare_integers(num5, num6))