def get_last_item(lst):
    if lst is None or len(lst) == 0:
        return None
    result = lst[0]
    for item in lst:
        result = item
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_item(sample_list))
    print(get_last_item([]))
    print(get_last_item([99]))