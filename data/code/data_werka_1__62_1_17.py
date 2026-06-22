def get_second_item(lst):
    INDEX_THRESHOLD = 1
    if len(lst) <= INDEX_THRESHOLD:
        raise IndexError("List does not have a second item.")
    return lst[INDEX_THRESHOLD]

if __name__ == '__main__':
    SAMPLE_LIST = [9, 19, 29]
    try:
        print(get_second_item(SAMPLE_LIST))
    except IndexError as e:
        print(e)