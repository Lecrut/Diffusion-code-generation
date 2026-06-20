def xnor(a: bool, b: bool) -> bool:
    return not (a ^ b)

if __name__ == '__main__':
    results = {
        (True, True): True,
        (False, False): True,
        (True, False): False,
        (False, True): False
    }
    
    for (bool1, bool2), expected in results.items():
        result = xnor(bool1, bool2)
        print(f"xnor({bool1}, {bool2}) = {result} (expected: {expected})")