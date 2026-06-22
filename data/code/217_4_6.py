def compare_numbers(a, b):
    return f"a {'>' if a > b else '<'} b" if a != b else "a == b"

if __name__ == '__main__':
    num1 = 34
    num2 = 56
    result = compare_numbers(num1, num2)
    print(result)