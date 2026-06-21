def evaluate_nested_flag(tuples):
    results = []
    for tup in tuples:
        flag1, flag2, flag3 = tup
        result = (flag1 and flag2) or not flag3
        results.append(result)
    return results

if __name__ == '__main__':
    sample_values = [(True, False, True), (False, True, False), (True, True, True)]
    print(evaluate_nested_flag(sample_values))