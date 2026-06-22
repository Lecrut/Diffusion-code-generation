def get_last_item(lst):
    if len(lst) == 0:
        return None
    last_index = len(lst) - 1
    return lst[last_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)