def find_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for x in data[1:]:
        if x > max_val:
            max_val = x
    return max_val

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2]
    sample_list2 = [-10, -5, -8, -2]
    sample_list3 = [7]
    sample_list4 = []

    max_of_sample1 = find_max(sample_list1)
    max_of_sample2 = find_max(sample_list2)
    max_of_sample3 = find_max(sample_list3)

    try:
        max_of_sample4 = find_max(sample_list4)
    except ValueError as e:
        max_of_sample4 = str(e)

    print(f"Max of {sample_list1}: {max_of_sample1}")
    print(f"Max of {sample_list2}: {max_of_sample2}")
    print(f"Max of {sample_list3}: {max_of_sample3}")
    print(f"Max of {sample_list4}: {max_of_sample4}")