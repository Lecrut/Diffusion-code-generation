def calculate_average_of_combined_sets(list_of_sets):
    all_numbers = set()
    for s in list_of_sets:
        all_numbers.update(s)
    if not all_numbers:
        return 0
    return sum(all_numbers) / len(all_numbers)
if __name__ == '__main__':
    sample_data = [
        {1, 2, 3},
        {3, 4, 5},
        {5, 6}
    ]
    average = calculate_average_of_combined_sets(sample_data)
    print(average)