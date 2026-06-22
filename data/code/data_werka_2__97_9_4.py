def generate_truth_table(a, b):
    results = []
    for val_a in [True, False]:
        for val_b in [True, False]:
            results.append((val_a, val_b, val_a and val_b, val_a or val_b, val_a != val_b))
    print("A     B     A and B A or B  A != B")
    print("-" * 35)
    for row in results:
        print(f"{str(row[0]):<5} {str(row[1]):<5} {str(row[2]):<7} {str(row[3]):<6} {str(row[4]):<6}")
    return results

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    generate_truth_table(sample_a, sample_b)