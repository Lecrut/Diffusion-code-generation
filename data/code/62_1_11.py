def get_second_item(lst):
    try:
        return lst[1]
    except IndexError:
        raise IndexError("List does not have a second item.")

if __name__ == '__main__':
    sample_list = [9, 19, 29]
    try:
        print(get_second_item(sample_list))
    except IndexError as e:
        print(e)