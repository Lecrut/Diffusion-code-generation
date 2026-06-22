def calculate_average_of_lists(list_of_lists):
    try:
        all_elements = sum(list_of_lists, [])
        total_sum = sum(all_elements)
        total_count = len(all_elements)
        if total_count == 0:
            return 0.0
        return float(total_sum / total_count)
    except TypeError:
        raise ValueError("Input must be a list of lists")

if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [4, 5]
    data3 = [6, 7, 8, 9]
    average = calculate_average_of_lists([data1, data2, data3])
    print(average)