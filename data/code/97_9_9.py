def generate_truth_table(a, b):
    results = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            results.append((val_a, val_b))
    for val_a, val_b in results:
        print(f"{val_a} {val_b}")
    return results

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    generate_truth_table(sample_a, sample_b)