def check_combined_conditions(bool1, bool2):
    return bool1 or bool2

if __name__ == '__main__':
    conditions = {
        (True, False): True,
        (False, True): True,
        (True, True): True,
        (False, False): False
    }
    
    for inputs, expected in conditions.items():
        result = check_combined_conditions(*inputs)
        print(f"check_combined_conditions({inputs[0]}, {inputs[1]}): {result} (Expected: {expected})")