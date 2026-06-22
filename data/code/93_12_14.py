def are_both_false(A: bool, B: bool) -> bool:
    return not A and not B

if __name__ == '__main__':
    A = False
    B = False
    result = are_both_false(A, B)
    print(result)