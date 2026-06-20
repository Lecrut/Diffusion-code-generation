def check_booleans(a: bool, b: bool) -> str:
    if a and b:
        return "Both are true"
    else:
        return "At least one is false"

if __name__ == '__main__':
    value1 = True
    value2 = False
    result = check_booleans(value1, value2)
    print(result)