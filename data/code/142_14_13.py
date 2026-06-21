def are_equivalent(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    x = True
    y = False
    print(are_equivalent(x, y))
    
    p = False
    q = False
    print(are_equivalent(p, q))