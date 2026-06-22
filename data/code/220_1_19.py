def calculate_average_of_lists(list_of_lists):
    total_sum = 0
    count = 0
    for lst in list_of_lists:
        if not lst:
            continue
        total_sum += sum(lst)
        count += len(lst)
    if count == 0:
        return 0.0
    return total_sum / count

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [3, 4, 5],
        [5, 6]
    ]
    average = calculate_average_of_lists(sample_data)
    print(average)