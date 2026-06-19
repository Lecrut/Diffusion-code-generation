def get_second_item(lst):
    MIN_LIST_LENGTH = 2
    if len(lst) < MIN_LIST_LENGTH:
        raise IndexError("List does not have a second item.")
    return lst[1]

if __name__ == '__main__':
    SAMPLE_LIST = [9, 19, 29]
    try:
        print(get_second_item(SAMPLE_LIST))
    except IndexError as e:
        print(e)