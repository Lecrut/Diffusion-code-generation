def check_or_conditions(conditions):
    results = []
    for condition1, condition2 in conditions:
        results.append(condition1 or condition2)
    return results

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False), (True, True)]
    print(check_or_conditions(sample_conditions))