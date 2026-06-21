def evaluate_flags(flag_tuples):
    results = []
    for flags in flag_tuples:
        result = (flags[0] or flags[1]) and not flags[2]
        results.append(result)
    return results

if __name__ == '__main__':
    sample_values = [
        (True, False, True),
        (False, True, False),
        (True, True, True),
        (False, False, False)
    ]
    print(evaluate_flags(sample_values))