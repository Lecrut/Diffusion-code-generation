def get_second_item(data):
    try:
        return data[1]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = ['a', 'b']
    sample_list3 = [True, False]
    sample_list4 = [42]
    sample_list5 = []
    print(get_second_item(sample_list1))
    print(get_second_item(sample_list2))
    print(get_second_item(sample_list3))
    print(get_second_item(sample_list4))
    print(get_second_item(sample_list5))