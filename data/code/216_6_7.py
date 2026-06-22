def median(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2.0
    else:
        return lst[mid]

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.1]
    print(median(sample_values))