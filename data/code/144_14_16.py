def evaluate_expression(A, B, C):
    return (A and B) or (not C)

def generate_truth_table():
    results = []
    for A in [True, False]:
        for B in [True, False]:
            for C in [True, False]:
                result = evaluate_expression(A, B, C)
                results.append({'A': A, 'B': B, 'C': C, 'Result': result})
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(row)