def join_lists(list_one, list_two):
    return list_one + list_two

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = join_lists(list_a, list_b)
    print(result)

    list_c = ['apple', 'banana', 'cherry']
    list_d = ['banana', 'date', 'elderberry']
    result2 = join_lists(list_c, list_d)
    print(result2)