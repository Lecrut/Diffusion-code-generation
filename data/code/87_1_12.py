def check_combined_conditions(bool1, bool2):
    return bool1 or bool2

if __name__ == '__main__':
    results = {
        (True, False): True,
        (False, True): True,
        (True, True): True,
        (False, False): False
    }
    for (condition1, condition2), expected in results.items():
        result = check_combined_conditions(condition1, condition2)
        print(f"check_combined_conditions({condition1}, {condition2}): {result} (Expected: {expected})")