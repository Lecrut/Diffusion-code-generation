def calculate_average_of_combined_set(list_of_sets):
    combined_set = set()
    for s in list_of_sets:
        combined_set.update(s)
    if not combined_set:
        return 0
    total_sum = sum(combined_set)
    count = len(combined_set)
    return total_sum / count
if __name__ == '__main__':
    sample_data = [
        {1, 2, 3},
        {3, 4, 5},
        {5, 6, 7}
    ]
    average = calculate_average_of_combined_set(sample_data)
    print(average)