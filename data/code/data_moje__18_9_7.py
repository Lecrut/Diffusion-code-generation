def get_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 1:
        return sorted_values[mid]
    return (sorted_values[mid - 1] + sorted_values[mid]) // 2

if __name__ == '__main__':
    list_one = [7, 1, 3, 9, 5]
    list_two = [4, 2, 8, 1, 6, 3]
    print(get_median(list_one))
    print(get_median(list_two))