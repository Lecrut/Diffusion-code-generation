def absolute_difference_generator(list1, list2):
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15, 25, 35]
    
    for diff in absolute_difference_generator(list1, list2):
        print(diff)