import collections
def process_conditions(conditions):
    results = collections.defaultdict(int)
    for condition in conditions:
        if condition:
            results['True'] += 1
        else:
            results['False'] += 1
    return dict(results)
if __name__ == '__main__':
    sample_conditions = [True, False, True, True, False, False, True]
    output = process_conditions(sample_conditions)
    print(output)