def timsort_ascending(lst):
    if not all(isinstance(x, int) for x in lst):
        raise ValueError("List must contain only integers.")
    return sorted(lst)

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    print("Original list:", sample_list)
    sorted_list = timsort_ascending(sample_list)
    print("Sorted list:", sorted_list)