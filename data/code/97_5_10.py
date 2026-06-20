def generate_truth_table():
    conditions = ['A', 'B', 'C', 'D']
    results = []

    for a in [True, False]:
        for b in [True, False]:
            for c in [True, False]:
                for d in [True, False]:
                    row = {'A': a, 'B': b, 'C': c, 'D': d}
                    results.append(row)

    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    for row in truth_table:
        print(row)