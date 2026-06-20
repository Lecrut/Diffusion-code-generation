def divide_lists(list1, list2):
    return [a / b for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [2, 4, 5]
    result = divide_lists(sample_list1, sample_list2)
    print(result)