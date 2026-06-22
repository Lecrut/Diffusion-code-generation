def are_both_false(a: bool, b: bool) -> bool:
    return not (a or b)

if __name__ == '__main__':
    A = False
    B = False
    result = are_both_false(A, B)
    print(result)