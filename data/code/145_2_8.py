def evaluate_flags(flag_tuples):
    results = []
    for flags in flag_tuples:
        result = (flags[0] and not flags[1]) or (not flags[2] and flags[3])
        results.append(result)
    return results

if __name__ == '__main__':
    sample_values = [
        (True, False, True, False),
        (False, True, False, True),
        (True, True, False, False),
        (False, False, True, True)
    ]
    print(evaluate_flags(sample_values))