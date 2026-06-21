def are_equivalent(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    TRUE = True
    FALSE = False
    
    print(are_equivalent(TRUE, TRUE))
    print(are_equivalent(TRUE, FALSE))
    print(are_equivalent(FALSE, TRUE))
    print(are_equivalent(FALSE, FALSE))