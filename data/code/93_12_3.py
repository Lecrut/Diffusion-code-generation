def both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    A = False
    B = False
    result = both_false(A, B)
    print(result)