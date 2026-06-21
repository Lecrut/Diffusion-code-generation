TARGET_ITEM = 2

def remove_item_from_list(input_list):
    return list(filter(lambda item: item != TARGET_ITEM, input_list))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 2, 4, 2, 5]
    result1 = remove_item_from_list(sample_list1)
    print(f"Original list: {sample_list1}")
    print(f"New list: {result1}")

    sample_list2 = ['a', 'b', 'c', 'a', 'd']
    result2 = remove_item_from_list(sample_list2)
    print(f"Original list: {sample_list2}")
    print(f"New list: {result2}")

    sample_list3 = [10, 20, 30, 40]
    result3 = remove_item_from_list(sample_list3)
    print(f"Original list: {sample_list3}")
    print(f"New list: {result3}")