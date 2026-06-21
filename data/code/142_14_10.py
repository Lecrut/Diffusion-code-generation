def are_equivalent(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    value1 = True
    value2 = False
    print(are_equivalent(value1, value2))
    
    value3 = False
    value4 = True
    print(are_equivalent(value3, value4))