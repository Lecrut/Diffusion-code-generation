def compare_booleans(a: bool, b: bool) -> str:
    return f"{a} is {'equal to' if a == b else 'not equal to'} {b}"

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)