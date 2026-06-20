def check_combined_conditions(bool1, bool2):
    return bool1 or bool2

if __name__ == '__main__':
    results = {
        (True, False): check_combined_conditions(True, False),
        (False, True): check_combined_conditions(False, True),
        (True, True): check_combined_conditions(True, True),
        (False, False): check_combined_conditions(False, False)
    }
    
    for key, value in results.items():
        print(f"check_combined_conditions{key}: {value}")