def common_elements_generator(iter1, iter2):
    set1 = set(iter1)
    for item in iter2:
        if item in set1:
            yield item

if __name__ == '__main__':
    list_a = [1, 5, 2, 8, 3, 9, 4, 7]
    list_b = [8, 3, 1, 9, 6, 2, 10, 5]
    common_gen = common_elements_generator(list_a, list_b)
    print(list(common_gen))