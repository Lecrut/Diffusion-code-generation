def compare_elements(first_list, second_list):
    MAX_INDEX = min(len(first_list), len(second_list))
    GREATER_THRESHOLD = 0
    matches = []
    index = 0
    while index < MAX_INDEX:
        val_first = first_list[index]
        val_second = second_list[index]
        if val_first > val_second:
            matches.append((val_first, val_second))
        index += 1
    return matches

if __name__ == '__main__':
    input_a = [15, 4, 9, 2]
    input_b = [10, 5, 8, 3]
    comparison_results = compare_elements(input_a, input_b)
    for first_val, second_val in comparison_results:
        print(f"{first_val} > {second_val}")