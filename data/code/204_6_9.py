import statistics
def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return None
    elif n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    sample_list = [3.5, 1.2, 8.9, 4.1, 2.3]
    median_value = find_median(sample_list)
    print(median_value)