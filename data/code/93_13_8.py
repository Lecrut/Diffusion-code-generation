def check_false(A: bool, B: bool) -> bool:
    return not A and not B

if __name__ == '__main__':
    x = False
    y = True
    result = check_false(x, y)
    print(result)