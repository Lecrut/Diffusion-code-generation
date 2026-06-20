def check_combined_conditions(bool1, bool2):
    return bool1 or bool2

if __name__ == '__main__':
    conditions = {
        (True, False): True,
        (False, True): True,
        (True, True): True,
        (False, False): False
    }
    
    for (bool1, bool2), expected in conditions.items():
        result = check_combined_conditions(bool1, bool2)
        print(f"check_combined_conditions({bool1}, {bool2}): {result} (Expected: {expected})")