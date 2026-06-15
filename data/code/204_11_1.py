import random
def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    median_value = find_median(sample_list)
    print(median_value)