def get_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    print(get_last_item(sample_data))
    empty_list = []
    print(get_last_item(empty_list))