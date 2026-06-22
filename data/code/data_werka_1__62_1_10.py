def get_second_item(lst):
    index_map = {0: "first", 1: "second"}
    try:
        return lst[1]
    except IndexError:
        raise IndexError(f"List does not have a {index_map[1]} item.")

if __name__ == '__main__':
    sample_list = [9, 19, 29]
    try:
        print(get_second_item(sample_list))
    except IndexError as e:
        print(e)