def check_false_pair(A: bool, B: bool) -> bool:
    if not A:
        return not B
    return False

if __name__ == '__main__':
    A = False
    B = False
    result = check_false_pair(A, B)
    print(result)