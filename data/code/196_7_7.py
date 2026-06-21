def concatenate_lists(list1, list2):
    for item in list1:
        yield item
    for item in list2:
        yield item

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    concatenated_gen = concatenate_lists(sample_list1, sample_list2)
    for item in concatenated_gen:
        print(item)