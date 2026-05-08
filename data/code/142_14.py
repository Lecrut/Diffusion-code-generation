import sys
def are_equivalent(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    a1 = True
    b1 = True
    print(are_equivalent(a1, b1))
    a2 = True
    b2 = False
    print(are_equivalent(a2, b2))
    a3 = False
    b3 = False
    print(are_equivalent(a3, b3))
    a4 = False
    b4 = True
    print(are_equivalent(a4, b4))
    a5 = True
    b5 = True
    print(are_equivalent(a5, b5))
    a6 = False
    b6 = False
    print(are_equivalent(a6, b6))