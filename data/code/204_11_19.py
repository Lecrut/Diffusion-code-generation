def find_median(data):
    n = len(data)
    if n == 0:
        return None
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        yield data[mid]
        if n % 2 == 1:
            return
        if data[mid] > data[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(next(find_median(sorted(list1))))
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(next(find_median(sorted(list2))))