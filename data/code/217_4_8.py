def compare_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    return f"a {'>' if a > b else '<'} b" if a != b else "a == b"

if __name__ == '__main__':
    num1 = 42
    num2 = 17
    print(compare_numbers(num1, num2))