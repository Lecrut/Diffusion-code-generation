def find_middle(lst):
    n = len(lst)
    if n == 0:
        raise ValueError("List must not be empty")
    mid_index = n // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = find_middle(sample_list)
    print(result)