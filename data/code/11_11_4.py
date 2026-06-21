def get_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    result1 = get_last_item(sample_list1)
    print(result1)

    sample_list2 = []
    result2 = get_last_item(sample_list2)
    print(result2)

    sample_list3 = [42]
    result3 = get_last_item(sample_list3)
    print(result3)