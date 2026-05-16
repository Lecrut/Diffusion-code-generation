import math
def find_median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
def filter_by_median(data):
    if not data:
        return []
    median_value = find_median(data)
    result = [x for x in data if x > median_value]
    return result
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3, 7, 4, 6]
    result = filter_by_median(sample_list)
    print(result)