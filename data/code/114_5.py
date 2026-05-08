def product_pairs(list1, list2):
    for a in list1:
        for b in list2:
            yield a * b
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result_generator = product_pairs(list_a, list_b)
    results = list(result_generator)
    print(results)