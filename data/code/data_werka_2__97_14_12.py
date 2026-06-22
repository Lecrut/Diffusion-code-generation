def generate_or_truth_table():
    inputs = [True, False]
    results = []
    for a in inputs:
        for b in inputs:
            results.append({'a': a, 'b': b, 'a OR b': a or b})
    return results

if __name__ == '__main__':
    print(generate_or_truth_table())