def compare_elements(list_a, list_b):
    comparisons = []
    for val_first, val_second in zip(list_a, list_b):
        status = ""
        if val_first < val_second:
            status = "less than"
        elif val_first > val_second:
            status = "greater than"
        else:
            status = "equal to"
        comparisons.append(f"{val_first} {status} {val_second}")
    return comparisons

if __name__ == '__main__':
    first_list = [10, 20, 30, 40, 50]
    second_list = [10, 15, 30, 45, 5]
    comparison_results = compare_elements(first_list, second_list)
    for line in comparison_results:
        print(line)