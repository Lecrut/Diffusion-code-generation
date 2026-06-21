def get_third_element(lst):
    if len(lst) < 3:
        raise IndexError("List has fewer than three items")
    return lst[2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        result = get_third_element(sample_list)
        print(result)
    except IndexError as e:
        print(e)

    short_list = [1, 2]
    try:
        result = get_third_element(short_list)
        print(result)
    except IndexError as e:
        print(e)