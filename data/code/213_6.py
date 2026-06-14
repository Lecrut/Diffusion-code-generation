def process_list(data):
    unique_numbers = set(data)
    frequency_distribution = {}
    for number in unique_numbers:
        frequency_distribution[number] = data.count(number)
    return frequency_distribution
if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 1, 4, 2, 5, 3, 1]
    result = process_list(sample_list)
    print(result)