def process_conditions(conditions):
    results = {'True': 0, 'False': 0}
    for condition in conditions:
        if condition:
            results['True'] += 1
        else:
            results['False'] += 1
    return results
if __name__ == '__main__':
    sample_conditions = [True, False, True, True, False, False, True]
    output = process_conditions(sample_conditions)
    print(output)