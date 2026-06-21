def calculate_average(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    average = calculate_average(sample_list)
    print(average)

    sample_list_empty = []
    average_empty = calculate_average(sample_list_empty)
    print(average_empty)

    sample_list_floats = [1.5, 2.5, 3.0]
    average_floats = calculate_average(sample_list_floats)
    print(average_floats)