def check_booleans(x: bool, y: bool) -> bool:
    return not x and not y

if __name__ == '__main__':
    result1 = check_booleans(False, False)
    result2 = check_booleans(True, True)
    
    print(f"check_booleans(False, False): {result1}")
    print(f"check_booleans(True, True): {result2}")