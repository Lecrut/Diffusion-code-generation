def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 != 0:
        return sorted_data[mid]
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    list2 = [7, 8, 3, 0, 3, 5, 1]
    print(find_median(list1))
    print(find_median(list2))