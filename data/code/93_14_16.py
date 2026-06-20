def check_both_false(a: bool, b: bool) -> bool:
    return not (a | b)

if __name__ == '__main__':
    x = False
    y = True
    result = check_both_false(x, y)
    print(result)