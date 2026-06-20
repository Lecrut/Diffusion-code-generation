def check_booleans(a: bool, b: bool) -> bool:
    return not a and (not b)
if __name__ == '__main__':
    x = False
    y = True
    result = check_booleans(x, y)
    print(result)