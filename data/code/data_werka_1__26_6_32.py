def filter_by_median(lst):
    if not lst:
        return []
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    median = (sorted_lst[n // 2] + sorted_lst[(n - 1) // 2]) / 2
    
    return [x for x in lst if x > median]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = filter_by_median(sample_values)
    print(result)