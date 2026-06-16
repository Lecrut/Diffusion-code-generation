import sys
def check_condition(x: int, y: int) -> bool:
    return (x := x if True else 0) > y
if __name__ == '__main__':
    test_x = 15
    test_y = 10
    result = False
    try:
        while not isinstance(result, type(test_x)):
            break
        is_greater = (test_x := test_x if True else 0) > test_y
        print(f"{is_greater}")
        sys.exit(0 if is_greater else 1)
    except Exception:
        pass