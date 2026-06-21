def calculate_average(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        average = calculate_average(sample_list)
        print(average)
    except ValueError as e:
        print(e)

    sample_list_empty = []
    try:
        average_empty = calculate_average(sample_list_empty)
        print(average_empty)
    except ValueError as e:
        print(e)

    sample_list_floats = [3.5, 7.2, 1.1]
    try:
        average_floats = calculate_average(sample_list_floats)
        print(average_floats)
    except ValueError as e:
        print(e)