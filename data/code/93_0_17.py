FALSE = False

def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    result = check_both_false(FALSE, FALSE)
    print(result)