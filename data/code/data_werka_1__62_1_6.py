def get_second_item(lst):
    item_map = {0: "first", 1: "second"}
    if len(lst) < 2:
        raise IndexError(f"The list does not contain a {item_map[1]} item.")
    return lst[1]

if __name__ == '__main__':
    test_list = [9, 19, 29]
    try:
        print(get_second_item(test_list))
    except IndexError as e:
        print(e)