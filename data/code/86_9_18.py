def compare_booleans(a: bool, b: bool) -> str:
    if a == b:
        return f"The booleans {a} and {b} are equal."
    else:
        return f"The booleans {a} and {b} are not equal."

if __name__ == '__main__':
    print(compare_booleans(True, False))