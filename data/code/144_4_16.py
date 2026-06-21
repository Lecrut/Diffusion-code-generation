def generate_truth_table():
    truth_values = ['True', 'False']
    combinations = [(a, b) for a in truth_values for b in truth_values]
    results = []
    for a, b in combinations:
        result = 'True' if not a or b else 'False'
        results.append((a, b, result))
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(row)