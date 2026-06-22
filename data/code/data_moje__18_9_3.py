def median_of_list(data):
    if not data:
        return None
    sorted_data = sorted(data)
    length = len(sorted_data)
    mid = (length - 1) // 2
    if length % 2 == 0:
        val1 = sorted_data[mid]
        val2 = sorted_data[mid + 1]
        return (val1 + val2) // 2
    else:
        return sorted_data[mid]

if __name__ == '__main__':
    sample1 = [1, 3, 5, 7, 9]
    sample2 = [2, 4, 6, 8]
    sample3 = [10]
    sample4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(median_of_list(sample1))
    print(median_of_list(sample2))
    print(median_of_list(sample3))
    print(median_of_list(sample4))