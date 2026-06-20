def check_or_conditions(conditions):
    results = []
    for condition in conditions:
        if condition[0] or condition[1]:
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_conditions = [(True, False), (False, True), (False, False), (True, True)]
    print(check_or_conditions(sample_conditions))