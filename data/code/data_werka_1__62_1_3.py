def get_second_item(lst):
    try:
        return lst[1]
    except IndexError:
        raise IndexError("List does not have a second item.")

if __name__ == '__main__':
    sample_list = [7, 17, 27]
    try:
        print(get_second_item(sample_list))
    except IndexError as e:
        print(e)