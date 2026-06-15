import random
def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (sorted_data[lower_middle_index] + sorted_data[upper_middle_index]) / 2
        return median
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    median_value = find_median(sample_list)
    print(median_value)