def calculate_average_of_lists(lists):
    total_sum = sum(sum(lst) for lst in lists if hasattr(lst, '__iter__'))
    total_count = sum(len(lst) for lst in lists if hasattr(lst, '__iter__'))
    return float(total_sum / total_count) if total_count > 0 else 0.0

if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [4, 5]
    data3 = [6, 7, 8, 9]
    lists_to_average = [data1, data2, data3]
    average = calculate_average_of_lists(lists_to_average)
    print(average)