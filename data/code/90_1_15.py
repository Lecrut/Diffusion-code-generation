def check_or_condition(a: bool, b: bool) -> bool:
    return a or b

if __name__ == '__main__':
    results = {
        (True, False): check_or_condition(True, False),
        (False, True): check_or_condition(False, True),
        (True, True): check_or_condition(True, True),
        (False, False): check_or_condition(False, False)
    }
    
    for inputs, result in results.items():
        print(f"check_or_condition{inputs}: {result}")