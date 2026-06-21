def evaluate_expression(a, b, c):
    return (a and b) or not c

def generate_truth_table():
    results = []
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                result = evaluate_expression(a, b, c)
                results.append({'A': a, 'B': b, 'C': c, 'Result': result})
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(row)