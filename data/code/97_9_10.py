def generate_truth_table(a, b):
    results = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            results.append((val_a, val_b))
    for row in results:
        print(row)

if __name__ == '__main__':
    generate_truth_table(True, False)