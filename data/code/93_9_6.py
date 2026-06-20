def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    results = {
        (False, False): "Both False",
        (True, False): "First True",
        (False, True): "Second True",
        (True, True): "Both True"
    }
    
    for (a1, b1), expected in results.items():
        result = check_both_false(a1, b1)
        print(f"({a1}, {b1}) -> {expected}: {result}")