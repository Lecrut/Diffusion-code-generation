def absolute_difference_generator(list1, list2):
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    sample_list_1 = [45, 60, 75, 90]
    sample_list_2 = [30, 45, 60, 75]
    for difference in absolute_difference_generator(sample_list_1, sample_list_2):
        print(difference)