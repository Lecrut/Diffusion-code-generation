def is_false_and_false(a: bool, b: bool) -> bool:
    lookup = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    return lookup[(a, b)]

if __name__ == '__main__':
    A = False
    B = False
    print(is_false_and_false(A, B))
    A = True
    B = False
    print(is_false_and_false(A, B))