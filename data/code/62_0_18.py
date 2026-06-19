def access_second_item(lst):
    SECOND_ITEM_INDEX = 1
    return lst[SECOND_ITEM_INDEX]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    result = access_second_item(sample_list)
    print(result)