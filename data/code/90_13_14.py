def check_or_condition(a: bool, b: bool) -> bool:
    return a | b

if __name__ == '__main__':
    x = True
    y = False
    result = check_or_condition(x, y)
    print(result)