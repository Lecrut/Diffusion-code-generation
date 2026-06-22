def get_second_item(lst):
    try:
        return lst[1]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = [5]
    print(get_second_item(sample_list_1))
    print(get_second_item(sample_list_2))