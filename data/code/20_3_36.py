def list_elementwise_equal(list1, list2):
    for item1, item2 in zip(list1, list2):
        yield (item1 == item2)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [1, 2, 3, 5]
    result_generator = list_elementwise_equal(list_a, list_b)
    results = list(result_generator)
    print(results)