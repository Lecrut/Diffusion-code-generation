def evaluate_boolean_tuples(tuples_list):
    results = []
    for a, b in tuples_list:
        if a and b:
            results.append(True)
        elif a and not b:
            results.append(False)
        elif not a and b:
            results.append(False)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_data = [(True, True), (True, False), (False, True), (False, False)]
    output = evaluate_boolean_tuples(sample_data)
    print(output)