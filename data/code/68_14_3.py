def absolute_difference_generator(list1, list2):
    for x in list1:
        for y in list2:
            yield abs(x - y)
if __name__ == '__main__':
    list_a = [1, 5, 10]
    list_b = [2, 4, 6]
    differences = absolute_difference_generator(list_a, list_b)
    results = list(differences)
    print(results)