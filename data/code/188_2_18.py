def reverse_using_iter(input_list):
    return list(reversed(input_list))

if __name__ == '__main__':
    test_list = ['a', 'b', 'c', 'd']
    reversed_test_list = reverse_using_iter(test_list)
    print(reversed_test_list)