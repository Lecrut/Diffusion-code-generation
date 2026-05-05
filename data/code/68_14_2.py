def absolute_difference_generator(list1, list2):
    for x in list1:
        for y in list2:
            yield abs(x - y)
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    diff_gen = absolute_difference_generator(list_a, list_b)
    results = list(diff_gen)
    print(results)