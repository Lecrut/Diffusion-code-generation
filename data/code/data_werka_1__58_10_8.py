def get_first_element(lst):
    try:
        return lst[0]
    except IndexError:
        raise ValueError("The list is empty")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_first_element(sample_list))