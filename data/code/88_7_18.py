def check_booleans(a: bool, b: bool) -> str:
    if a and b:
        return "Both are true"
    else:
        return "At least one is false"

if __name__ == '__main__':
    result = check_booleans(True, True)
    print(result)