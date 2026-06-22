def median_of(lst):
    if not lst:
        return None
    sorted_list = sorted(lst)
    count = len(sorted_list)
    mid = count // 2
    if count % 2 == 1:
        return sorted_list[mid]
    return sorted_list[mid - 1]

if __name__ == '__main__':
    print(median_of([3, 1, 4]))
    print(median_of([10, 20, 30, 40]))
    print(median_of([5]))
    print(median_of([1, 2, 3, 4, 5, 6]))
    print(median_of([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(median_of([]))