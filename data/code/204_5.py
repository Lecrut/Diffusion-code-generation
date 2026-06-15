def middle_element(iterable):
    n = len(iterable)
    if n % 2 == 1:
        yield iterable[n // 2]
    else:
        yield iterable[n // 2 - 1]
    return
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(list1)
    for element in middle_element(list1):
        print(element)
    list2 = [10, 20, 30, 40]
    print(list2)
    for element in middle_element(list2):
        print(element)
    list3 = [100]
    print(list3)
    for element in middle_element(list3):
        print(element)