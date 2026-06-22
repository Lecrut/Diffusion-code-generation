def calculate_average_of_lists(list_of_lists):
    if not all(isinstance(lst, list) for lst in list_of_lists):
        raise ValueError("All elements must be lists")
    total_sum = sum(sum(sublist) for sublist in list_of_lists)
    total_count = sum(len(sublist) for sublist in list_of_lists)
    if total_count == 0:
        return 0
    average = total_sum / total_count
    return round(average, 2)

if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [4, 5]
    data3 = [6, 7, 8, 9]
    average = calculate_average_of_lists([data1, data2, data3])
    print(average)