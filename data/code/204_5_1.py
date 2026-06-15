def middle_element(iterable):
    n = len(iterable)
    if n % 2 == 1:
        yield iterable[n // 2]
    else:
        yield iterable[n // 2 - 1]
    return
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    print(list_a)
    for element in middle_element(list_a):
        print(element)
    list_b = [10, 20, 30, 40]
    print(list_b)
    for element in middle_element(list_b):
        print(element)