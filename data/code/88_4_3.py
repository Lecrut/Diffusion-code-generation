def logical_and(val1: bool, val2: bool) -> bool:
    result = val1 and val2
    return result

if __name__ == '__main__':
    sample1 = logical_and(True, True)
    print(f"True AND True = {sample1}")
    
    sample2 = logical_and(True, False)
    print(f"True AND False = {sample2}")
    
    sample3 = logical_and(False, True)
    print(f"False AND True = {sample3}")
    
    sample4 = logical_and(False, False)
    print(f"False AND False = {sample4}")