def reverse_using_iter(lst):
    return list(reversed(lst))

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    reversed_list = reverse_using_iter(SAMPLE_LIST)
    print(reversed_list)