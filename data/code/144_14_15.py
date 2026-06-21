def evaluate_expression(a, b, c):
    return (a & b) | (~c)

def generate_truth_table():
    results = []
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                result = evaluate_expression(a, b, c)
                results.append({'A': a, 'B': b, 'C': c, 'Result': result})
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    print(truth_table)