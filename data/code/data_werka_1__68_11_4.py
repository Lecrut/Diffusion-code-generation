def absolute_difference_generator(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    try:
        list1 = [15, 30, 45, 60]
        list2 = [10, 25, 40, 55]
        for diff in absolute_difference_generator(list1, list2):
            print(diff)
    except ValueError as e:
        print(e)