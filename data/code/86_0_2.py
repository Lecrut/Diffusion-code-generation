def compare_booleans(a: bool, b: bool) -> str:
    return "True" if a == b else "False"

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)