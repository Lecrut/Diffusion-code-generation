def compare_booleans(a: bool, b: bool) -> str:
    if a == b:
        return f"The booleans are equal: {a}"
    else:
        return f"The booleans are different: {a} != {b}"

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)