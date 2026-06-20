def elementwise_division(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of equal length')
    return [x / y for x, y in zip(list1, list2)]
if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [2, 4, 5]
    result = elementwise_division(sample_list1, sample_list2)
    print(result)