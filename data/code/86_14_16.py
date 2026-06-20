def logical_equivalence(a: bool, b: bool) -> bool:
    return not (a ^ b)

if __name__ == '__main__':
    x = True
    y = False
    print(logical_equivalence(x, y))