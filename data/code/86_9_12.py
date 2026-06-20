def compare_booleans(a: bool, b: bool) -> str:
    if a == b:
        return "The booleans are equal."
    else:
        return "The booleans are not equal."

if __name__ == '__main__':
    result = compare_booleans(True, False)
    print(result)