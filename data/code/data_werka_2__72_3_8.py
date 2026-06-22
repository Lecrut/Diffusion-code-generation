def compare_and_print_greater(list_a, list_b):
    results = []
    length = min(len(list_a), len(list_b))
    for index in range(length):
        val_a = list_a[index]
        val_b = list_b[index]
        if val_a > val_b:
            results.append((val_a, val_b))
            print(f"{val_a} > {val_b}")
    return results

if __name__ == '__main__':
    sample_a = [10, 5, 8, 3]
    sample_b = [2, 6, 9, 1]
    output = compare_and_print_greater(sample_a, sample_b)
    print(output)