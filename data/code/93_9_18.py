def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    results = {
        (False, False): check_both_false(False, False),
        (True, False): check_both_false(True, False),
        (True, True): check_both_false(True, True),
        (False, True): check_both_false(False, True)
    }
    
    for (a, b), result in results.items():
        print(f"check_both_false({a}, {b}): {result}")