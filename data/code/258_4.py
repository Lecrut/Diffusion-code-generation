def calculate_averages(data):
    first_elements = [item[0] for item in data]
    second_elements = [item[1] for item in data]
    average_first = sum(first_elements) / len(first_elements) if first_elements else 0
    average_second = sum(second_elements) / len(second_elements) if second_elements else 0
    return (average_first, average_second)
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5, 6]]
    result = calculate_averages(sample_data)
    print(result)