def absolute_difference_generator(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    sample_data = {
        'group1': [8, 16, 24, 32],
        'group2': [4, 8, 12, 16]
    }
    try:
        for diff in absolute_difference_generator(sample_data['group1'], sample_data['group2']):
            print(diff)
    except ValueError as e:
        print(e)