def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    mid_index = length // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = find_middle(sample_list)
    print(result)