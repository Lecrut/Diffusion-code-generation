def concatenate_lists(list1, list2):
    it1 = iter(list1)
    it2 = iter(list2)
    while True:
        try:
            item1 = next(it1)
            yield item1
        except StopIteration:
            try:
                item2 = next(it2)
                yield item2
            except StopIteration:
                break
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result_generator = concatenate_lists(list_a, list_b)
    result_list = list(result_generator)
    print(result_list)