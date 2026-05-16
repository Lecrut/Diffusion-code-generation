def product_generator(list1, list2):
    for x in list1:
        for y in list2:
            yield x * y
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result_generator = product_generator(list_a, list_b)
    results = list(result_generator)
    print(results)