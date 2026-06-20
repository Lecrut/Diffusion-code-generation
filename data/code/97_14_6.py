def or_truth_table():
    inputs = [True, False]
    return [{'A': a, 'B': b, 'A OR B': a or b} for a in inputs for b in inputs]

if __name__ == '__main__':
    print(or_truth_table())