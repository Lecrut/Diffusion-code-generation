def check_both_true(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    results = {
        (True, True): True,
        (False, True): False,
        (True, False): False,
        (False, False): False
    }
    
    for inputs, expected in results.items():
        result = check_both_true(*inputs)
        print(f"check_both_true{inputs} -> {result}, Expected: {expected}")