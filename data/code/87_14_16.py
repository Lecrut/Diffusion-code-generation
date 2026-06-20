def exclusive_truthiness(flag_x: bool, flag_y: bool) -> bool:
    return flag_x ^ flag_y

if __name__ == '__main__':
    result1 = exclusive_truthiness(True, False)
    print(f"Result 1 (True, False): {result1}")
    
    result2 = exclusive_truthiness(False, True)
    print(f"Result 2 (False, True): {result2}")
    
    result3 = exclusive_truthiness(True, True)
    print(f"Result 3 (True, True): {result3}")
    
    result4 = exclusive_truthiness(False, False)
    print(f"Result 4 (False, False): {result4}")