def get_third_item(lst):
    if len(lst) > 2:
        return lst[2]
    return None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_third_item(sample_list))