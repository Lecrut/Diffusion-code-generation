def evaluate_expression(expression):
    if expression == 'A AND B':
        return True & 1
    elif expression == 'OR C':
        return False | 1
    elif expression == '(A AND B) OR (NOT C)':
        return (True & 1) | (False ^ 1)
    else:
        raise ValueError("Invalid expression")

def generate_truth_table():
    results = []
    for A in [0, 1]:
        for B in [0, 1]:
            for C in [0, 1]:
                result = evaluate_expression('(A AND B) OR (NOT C)')
                results.append({'A': A, 'B': B, 'C': C, 'Result': result})
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(row)