def generate_truth_table(a, b):
    results = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            results.append((val_a, val_b, val_a and val_b, val_a or val_b, val_a != val_b))
    for row in results:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    return results

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    generate_truth_table(sample_a, sample_b)