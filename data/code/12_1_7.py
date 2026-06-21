def get_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0

if __name__ == '__main__':
    sample_values = [7, 1, 3, 4, 2, 6, 5]
    print(get_median(sample_values))