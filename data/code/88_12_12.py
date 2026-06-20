def check_both_true(a: bool, b: bool) -> bool:
    return a & b

if __name__ == '__main__':
    x = True
    y = False
    print(f"check_both_true({x}, {y}): {check_both_true(x, y)}")
    x = False
    y = True
    print(f"check_both_true({x}, {y}): {check_both_true(x, y)}")
    x = False
    y = False
    print(f"check_both_true({x}, {y}): {check_both_true(x, y)}")