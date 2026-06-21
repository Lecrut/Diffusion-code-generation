def are_equivalent(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    x = True
    y = False
    result1 = are_equivalent(x, y)
    print(result1)

    u = False
    v = False
    result2 = are_equivalent(u, v)
    print(result2)

    w = True
    z = True
    result3 = are_equivalent(w, z)
    print(result3)

    a = False
    b = True
    result4 = are_equivalent(a, b)
    print(result4)