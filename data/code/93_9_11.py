def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    x = False
    y = True
    result = check_both_false(x, y)
    print(f"check_both_false({x}, {y}): {result}")