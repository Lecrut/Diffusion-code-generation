def both_false(a: bool, b: bool) -> bool:
    return not a and not b
if __name__ == '__main__':
    x = False
    y = False
    result = both_false(x, y)
    print(result)