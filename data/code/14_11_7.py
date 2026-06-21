def get_third_item_safe(items):
    try:
        return items[2]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_list_short = [1, 2]
    print(get_third_item_safe(sample_list))
    print(get_third_item_safe(sample_list_short))