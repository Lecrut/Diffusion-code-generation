def combine_checks(is_positive, is_even, is_less_than_100):
    if not all(isinstance(i, bool) for i in [is_positive, is_even, is_less_than_100]):
        raise ValueError("All inputs must be boolean.")
    
    summary = []
    if is_positive:
        summary.append("Positive")
    if is_even:
        summary.append("Even")
    if is_less_than_100:
        summary.append("Less than 100")
    
    return ", ".join(summary) if summary else "No conditions met"

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, True, False))
    print(combine_checks(True, False, True))
    print(combine_checks(False, False, False))