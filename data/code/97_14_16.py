OR_INPUTS = [True, False]

def generate_or_truth_table(values):
    results = []
    for a in values:
        for b in values:
            or_result = a or b
            results.append({'a': a, 'b': b, 'or_result': or_result})
    return results

if __name__ == '__main__':
    truth_table = generate_or_truth_table(OR_INPUTS)
    print("a | b | a OR b")
    for row in truth_table:
        print(f"{row['a']} | {row['b']} | {row['or_result']}")