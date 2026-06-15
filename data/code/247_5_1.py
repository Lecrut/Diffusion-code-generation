def sum_all_pairs(list1, list2):
    for x in list1:
        for y in list2:
            yield x + y
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5]
    result_generator = sum_all_pairs(list_a, list_b)
    total_sum = sum(result_generator)
    print(total_sum)