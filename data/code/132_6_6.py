def verify_status(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    results = {
        (True, False): True,
        (False, True): True,
        (True, True): False,
        (False, False): False
    }
    
    for key, expected in results.items():
        result = verify_status(*key)
        print(f"verify_status({key[0]}, {key[1]}) = {result}, Expected: {expected}, Pass: {result == expected}")