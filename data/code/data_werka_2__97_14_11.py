def generate_or_truth_table():
    inputs = [True, False]
    table = []
    for a in inputs:
        for b in inputs:
            table.append({'a': a, 'b': b, 'a OR b': a or b})
    return table

if __name__ == '__main__':
    result = generate_or_truth_table()
    print(result)