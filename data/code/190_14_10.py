ITEM_CHECK_THRESHOLD = 100

def contains_item(lst, value):
    if len(lst) > ITEM_CHECK_THRESHOLD:
        return value in set(lst)
    return value in lst

if __name__ == '__main__':
    sample_list = [i for i in range(150)]
    print(contains_item(sample_list, 75))
    print(contains_item(sample_list, 200))