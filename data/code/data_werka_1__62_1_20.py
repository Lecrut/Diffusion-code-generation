def get_second_item(lst):
    MIN_LIST_LENGTH = 2
    SECOND_ITEM_INDEX = 1
    
    if len(lst) < MIN_LIST_LENGTH:
        raise IndexError("List does not have a second item.")
    return lst[SECOND_ITEM_INDEX]

if __name__ == '__main__':
    sample_list = [9, 19, 29]
    try:
        print(get_second_item(sample_list))
    except IndexError as e:
        print(e)