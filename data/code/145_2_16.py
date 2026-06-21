def evaluate_flags(flag_list):
    results = []
    for flags in flag_list:
        result = (not flags[0] and flags[1]) or (flags[2] and not flags[3])
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