def or_truth_table():
    inputs = [True, False]
    return [{'a': a, 'b': b, 'result': a or b} for a in inputs for b in inputs]

if __name__ == '__main__':
    print(or_truth_table())