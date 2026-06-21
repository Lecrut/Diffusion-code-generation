def calculate_average(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    average = calculate_average(sample_list)
    print(average)

    sample_list_empty = []
    average_empty = calculate_average(sample_list_empty)
    print(average_empty)

    sample_list_floats = [2.0, 4.0, 6.0]
    average_floats = calculate_average(sample_list_floats)
    print(average_floats)