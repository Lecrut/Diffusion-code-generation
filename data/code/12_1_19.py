def get_median(data):
    if not data:
        raise ValueError("List must not be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

if __name__ == '__main__':
    sample_list = [12, 4, 5, 3, 7, 1, 9]
    result = get_median(sample_list)
    print(result)