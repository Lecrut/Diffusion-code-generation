def iteratively_sort_tuple(data):
    sorted_list = []
    for _ in range(len(data)):
        min_value = min(data)
        sorted_list.append(min_value)
        data.remove(min_value)
    return sorted_list

if __name__ == '__main__':
    sample_data = [34, 7, 23, 32, 5, 62]
    sorted_result = iteratively_sort_tuple(sample_data)
    print(sorted_result)