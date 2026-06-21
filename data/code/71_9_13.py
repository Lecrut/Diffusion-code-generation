def find_middle_element(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List must not be empty")
    n = len(lst)
    index = (n - 1) // 2
    return lst[index]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5, 6, 7]
    sample_even = [10, 20, 30, 40, 50, 60]
    result_odd = find_middle_element(sample_odd)
    result_even = find_middle_element(sample_even)
    print(result_odd)
    print(result_even)