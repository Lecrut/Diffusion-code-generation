def calculate_average_of_all_elements(list_of_sets):
    total_sum = 0
    total_count = 0
    for s in list_of_sets:
        total_sum += sum(s)
        total_count += len(s)
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    sample_sets = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    average = calculate_average_of_all_elements(sample_sets)
    print(average)