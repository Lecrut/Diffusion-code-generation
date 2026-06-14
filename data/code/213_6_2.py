def process_and_calculate_frequency(data):
    unique_numbers = set(data)
    frequency_distribution = {}
    for number in unique_numbers:
        frequency_distribution[number] = data.count(number)
    return frequency_distribution
if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 1, 4, 2, 5, 3, 1, 6]
    result = process_and_calculate_frequency(sample_list)
    print(result)