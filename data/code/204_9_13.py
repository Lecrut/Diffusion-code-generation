def is_valid_list(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    return True

def find_median(lst):
    is_valid_list(lst)
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2.0
    else:
        return float(sorted_lst[mid])

if __name__ == '__main__':
    sample_list_odd = [3, 1, 4, 1, 5, 9, 2]
    print(f"Median of {sample_list_odd}: {find_median(sample_list_odd)}")
    
    sample_list_even = [1, 2, 3, 4, 5, 6]
    print(f"\nMedian of {sample_list_even}: {find_median(sample_list_even)}")