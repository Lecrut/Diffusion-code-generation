def check_both_false(a: bool, b: bool) -> bool:
    return not a | b
if __name__ == '__main__':
    A = True
    B = False
    result = check_both_false(A, B)
    print(result)