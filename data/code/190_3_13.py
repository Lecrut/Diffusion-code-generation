def check_membership(iterable, value):
    return value in iterable

if __name__ == '__main__':
    list1 = [1.1, 2.2, 3.3, 4.4, 5.5]
    value1 = 3.3
    result1 = check_membership(list1, value1)
    print(f"Is {value1} in {list1}? {result1}")

    list2 = [10.1, 20.2, 30.3]
    value2 = 5.5
    result2 = check_membership(list2, value2)
    print(f"Is {value2} in {list2}? {result2}")