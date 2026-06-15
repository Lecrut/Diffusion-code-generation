def sum_of_pairs_generator(list1, list2):
    for a in list1:
        for b in list2:
            yield a + b
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5]
    result_generator = sum_of_pairs_generator(list_a, list_b)
    total_sum = sum(result_generator)
    print(total_sum)