def median_index(lst):
    n = len(lst)
    if n == 0:
        return None
    if n % 2 == 1:
        return (n - 1) // 2
    left = n // 2 - 1
    right = n // 2
    return [left, right]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = median_index(sample_list)
    print(result)
    sample_list_odd = [10, 20, 30, 40, 50]
    result_odd = median_index(sample_list_odd)
    print(result_odd)
    sample_list_empty = []
    result_empty = median_index(sample_list_empty)
    print(result_empty)