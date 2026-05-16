import math
def find_median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
def filter_greater_than_median(data):
    if not data:
        return []
    median_value = find_median(data)
    result = [x for x in data if x > median_value]
    return result
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9, 11]
    result = filter_greater_than_median(sample_list)
    print(result)
    sample_list_2 = [1, 2, 3, 4, 5, 6, 7]
    result_2 = filter_greater_than_median(sample_list_2)
    print(result_2)
    sample_list_3 = [10, 20, 30, 40, 50]
    result_3 = filter_greater_than_median(sample_list_3)
    print(result_3)
    sample_list_4 = [1, 2, 8, 10, 12]
    result_4 = filter_greater_than_median(sample_list_4)
    print(result_4)