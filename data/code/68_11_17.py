def absolute_difference_generator(list1, list2):
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    list1 = [5, 3, 9, 1]
    list2 = [2, 8, 4, 7]
    
    for diff in absolute_difference_generator(list1, list2):
        print(diff)