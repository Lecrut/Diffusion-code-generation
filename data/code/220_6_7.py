def calculate_average(set_of_numbers):
    if not set_of_numbers:
        return 0
    total_sum = sum(set_of_numbers)
    count = len(set_of_numbers)
    return total_sum / count

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    average_result = calculate_average(sample_set)
    print(average_result)