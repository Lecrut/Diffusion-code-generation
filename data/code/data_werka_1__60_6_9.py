def get_last_element(lst):
    try:
        return lst[-1]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    empty_list = []
    print(get_last_element(sample_list))
    print(get_last_element(empty_list))