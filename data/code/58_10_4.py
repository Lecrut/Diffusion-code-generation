def get_first_element(lst):
    try:
        return lst[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [9, 18, 27, 36]
    print(get_first_element(sample_list))