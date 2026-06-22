def generate_or_truth_table():
    inputs = [True, False]
    result = []
    for a in inputs:
        for b in inputs:
            result.append({'a': a, 'b': b, 'a OR b': a or b})
    return result

if __name__ == '__main__':
    print(generate_or_truth_table())