def validate_list(list_of_lists):
    if not all(isinstance(sublist, list) for sublist in list_of_lists):
        raise ValueError("All elements must be lists")
    if any(not isinstance(item, int) for sublist in list_of_lists for item in sublist):
        raise ValueError("All elements in sublists must be integers")

def calculate_average(list_of_lists):
    total_sum = 0
    count = 0
    validate_list(list_of_lists)
    for sublist in list_of_lists:
        total_sum += sum(sublist)
        count += len(sublist)
    if count == 0:
        return 0.0
    return total_sum / count

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [3, 4, 5],
        [5, 6]
    ]
    average = calculate_average(sample_data)
    print(average)