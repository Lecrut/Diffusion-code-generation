def combine_checks(is_positive, is_even, is_less_than_100):
    results = []
    if is_positive:
        results.append("positive")
    if is_even:
        results.append("even")
    if is_less_than_100:
        results.append("less than 100")
    
    if not results:
        return "none"
    
    return " and ".join(results)

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, False, False))
    print(combine_checks(True, False, False))
    print(combine_checks(False, True, True))