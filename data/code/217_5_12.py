def compare(a: int, b: int) -> int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numeric")
    return 1 if a > b else -1 if a < b else 0

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(compare(num1, num2))
    
    num1 = 10
    num2 = 10
    print(compare(num1, num2))
    
    num1 = 1
    num2 = 10
    print(compare(num1, num2))