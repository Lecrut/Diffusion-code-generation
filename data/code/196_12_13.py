def merge_string_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    first_list = ["red", "green"]
    second_list = ["blue", "yellow"]
    combined_list = merge_string_lists(first_list, second_list)
    print(combined_list)