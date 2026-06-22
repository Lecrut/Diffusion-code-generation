def get_second_item(lst):
    if len(lst) < 2:
        raise IndexError("List does not have a second item.")
    return lst[1]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    try:
        print(get_second_item(sample_list))
    except IndexError as e:
        print(e)