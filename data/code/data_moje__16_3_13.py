def get_first_item(lst):
    if lst:
        return lst[0]
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    print(get_first_item(sample_list))