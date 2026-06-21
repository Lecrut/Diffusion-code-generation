def evaluate_expression(a, b, c):
    return (a and b) or not c

def generate_truth_table():
    truth_table = []
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                result = evaluate_expression(a, b, c)
                truth_table.append({'A': a, 'B': b, 'C': c, 'Result': result})
    return truth_table

if __name__ == '__main__':
    table = generate_truth_table()
    print(table)