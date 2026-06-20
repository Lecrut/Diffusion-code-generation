TRUE = True
FALSE = False

def logical_equivalence(a: bool, b: bool) -> bool:
    return (a and b) or (not a and not b)

if __name__ == '__main__':
    print(logical_equivalence(TRUE, TRUE))
    print(logical_equivalence(FALSE, FALSE))
    print(logical_equivalence(TRUE, FALSE))