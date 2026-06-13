def check_membership(iterable, value):
    return value in iterable
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    value1 = 3
    result1 = check_membership(list1, value1)
    print(f"Is {value1} in {list1}? {result1}")
    list2 = ['a', 'b', 'c']
    value2 = 'd'
    result2 = check_membership(list2, value2)
    print(f"Is {value2} in {list2}? {result2}")
    tuple1 = (10, 20, 30)
    value3 = 20
    result3 = check_membership(tuple1, value3)
    print(f"Is {value3} in {tuple1}? {result3}")