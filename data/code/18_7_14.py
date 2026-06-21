def get_middle_item(lst):
    if not lst:
        raise ValueError("List is empty")
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_list)
    print(result)