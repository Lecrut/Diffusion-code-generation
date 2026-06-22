def find_middle_element(lst):
    n = len(lst)
    if n == 0:
        raise ValueError("List must not be empty")
    mid_index = n // 2
    middle_slice = lst[mid_index - (1 if n % 2 == 0 else 0):mid_index + 1]
    return middle_slice[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = find_middle_element(sample_list)
    print(result)