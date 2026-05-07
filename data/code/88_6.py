def logical_and(a: bool, b: bool) -> bool:
    return a and b
if __name__ == '__main__':
    result1 = logical_and(True, True)
    print(f"logical_and(True, True): {result1}")
    result2 = logical_and(True, False)
    print(f"logical_and(True, False): {result2}")
    result3 = logical_and(False, True)
    print(f"logical_and(False, True): {result3}")
    result4 = logical_and(False, False)
    print(f"logical_and(False, False): {result4}")