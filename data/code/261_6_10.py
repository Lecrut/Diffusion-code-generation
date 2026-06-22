def median(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2.0
    else:
        return float(lst[mid])

if __name__ == '__main__':
    print(median([3, 1, 4, 1, 5, 9, 2]))
    print(median([1, 2, 3, 4, 5]))