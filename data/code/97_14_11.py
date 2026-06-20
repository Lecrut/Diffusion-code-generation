def generate_or_truth_table():
    inputs = [True, False]
    truth_table = [{'A': a, 'B': b, 'A or B': a or b} for a in inputs for b in inputs]
    return truth_table

if __name__ == '__main__':
    print(generate_or_truth_table())