def find_median(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) // 2
    return sorted_list[mid]

if __name__ == '__main__':
    print(find_median([1, 3, 2]))
    print(find_median([1, 2, 3, 4]))
    print(find_median([5, 1, 5, 3, 2]))
    print(find_median([10]))