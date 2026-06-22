def compare_numbers(a, b):
    result = f"a {'>' if a > b else '<'} b" if a != b else "a == b"
    return result

if __name__ == '__main__':
    num1 = 23
    num2 = 45
    print(compare_numbers(num1, num2))