def calculate_averages(data):
    if not data:
        return (0.0, 0.0)
    first_elements = [item[0] for item in data]
    second_elements = [item[1] for item in data]
    avg_first = sum(first_elements) / len(first_elements)
    avg_second = sum(second_elements) / len(second_elements)
    return avg_first, avg_second
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    avg1, avg2 = calculate_averages(sample_data)
    print(f"{avg1=}")
    print(f"{avg2=}")