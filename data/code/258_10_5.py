import math
def calculate_average_of_all_numbers(list_of_pairs):
    total_sum = 0
    total_count = 0
    for pair in list_of_pairs:
        total_sum += sum(pair)
        total_count += len(pair)
    if total_count == 0:
        return 0
    return total_sum / total_count
if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4, 5),
        (6, 7)
    ]
    average = calculate_average_of_all_numbers(sample_data)
    print(average)