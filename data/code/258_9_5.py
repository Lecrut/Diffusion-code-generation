def calculate_averages(data):
    if not data:
        return (0.0, 0.0)
    first_elements = [pair[0] for pair in data]
    second_elements = [pair[1] for pair in data]
    avg_first = sum(first_elements) / len(first_elements)
    avg_second = sum(second_elements) / len(second_elements)
    return (avg_first, avg_second)
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    result = calculate_averages(sample_data)
    print(result)