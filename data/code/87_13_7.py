def check_conditions(a: bool, b: bool) -> bool:
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    sample_values = {
        'True False': (True, False),
        'False True': (False, True),
        'True True': (True, True),
        'False False': (False, False)
    }
    
    results = {key: check_conditions(*value) for key, value in sample_values.items()}
    print(results)