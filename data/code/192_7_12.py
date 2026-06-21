def common_elements_generator(iterable1, iterable2):
    set2 = set(iterable2)
    for item in iterable1:
        if item in set2:
            yield item

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    common_gen = common_elements_generator(sample_list1, sample_list2)
    print(list(common_gen))