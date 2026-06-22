def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = find_middle(sample_list)
    print(result)