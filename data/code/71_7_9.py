def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = 0
    for _ in lst:
        length += 1
    mid_index = length // 2
    index = 0
    result = None
    for item in lst:
        if index == mid_index:
            result = item
            break
        index += 1
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    middle_value = find_middle(sample_list)
    print(middle_value)