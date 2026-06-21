def get_third_element(lst):
    if len(lst) < 3:
        raise IndexError("List must have at least three items")
    return lst[2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_third_element(sample_list))
    short_list = [1, 2]
    try:
        get_third_element(short_list)
    except IndexError as e:
        print(e)