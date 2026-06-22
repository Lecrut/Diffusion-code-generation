def get_last_item(lst):
    if not lst:
        return None
    index = len(lst) - 1
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)