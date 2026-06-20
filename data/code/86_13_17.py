def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    TRUE = True
    FALSE = False
    print(compare_booleans(TRUE, TRUE))
    print(compare_booleans(FALSE, FALSE))
    print(compare_booleans(TRUE, FALSE))