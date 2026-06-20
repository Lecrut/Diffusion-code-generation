def check_or_condition(a: bool, b: bool) -> bool:
    return a or b

if __name__ == '__main__':
    conditions = {
        (True, False): True,
        (False, True): True,
        (True, True): True,
        (False, False): False
    }
    
    for inputs, expected in conditions.items():
        result = check_or_condition(*inputs)
        print(f"check_or_condition{inputs}: {result}, Expected: {expected}")