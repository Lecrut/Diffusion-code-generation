def compare_elements(list_a, list_b):
    comparisons = []
    for val_a, val_b in zip(list_a, list_b):
        if val_a < val_b:
            comparisons.append(f"{val_a} < {val_b}")
        elif val_a > val_b:
            comparisons.append(f"{val_a} > {val_b}")
        else:
            comparisons.append(f"{val_a} == {val_b}")
    return comparisons

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [10, 15, 35, 5]
    result = compare_elements(sample_list_1, sample_list_2)
    for line in result:
        print(line)