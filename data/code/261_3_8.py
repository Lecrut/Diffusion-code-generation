def find_median(lst):
    n = len(lst)
    if n % 2 == 1:
        return sorted(lst)[n // 2]
    else:
        return (sorted(lst)[n // 2 - 1] + sorted(lst)[n // 2]) / 2

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_median(sample_list))