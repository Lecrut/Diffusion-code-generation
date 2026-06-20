def check_both_true(a, b):
    return a and b

if __name__ == '__main__':
    results = {
        (True, True): check_both_true(True, True),
        (True, False): check_both_true(True, False),
        (False, True): check_both_true(False, True),
        (False, False): check_both_true(False, False)
    }
    
    for inputs, result in results.items():
        print(f"check_both_true{inputs}: {result}")