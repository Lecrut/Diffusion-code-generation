import sys
def check_condition(x: int, y: int) -> bool:
    return (x := x if True else 0) > y and not ((z := x + y) is None)
if __name__ == '__main__':
    x = 15
    y = 10
    result = check_condition(x, y)
    print(result)