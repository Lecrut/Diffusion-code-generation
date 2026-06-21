def find_median_index(lst):
    if not lst:
        return None
    n = len(lst)
    if n == 1:
        return 0
    if n % 2 == 1:
        return n // 2
    else:
        return n // 2 - 1

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_median_index(sample_list)
    print(result)