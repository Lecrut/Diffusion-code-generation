def check_membership(iterable, value):
    return value in iterable
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    value1 = 3
    result1 = check_membership(list1, value1)
    print(f"Is {value1} in {list1}? {result1}")
    list2 = ['a', 'b', 'c']
    value2 = 'c'
    result2 = check_membership(list2, value2)
    print(f"Is {value2} in {list2}? {result2}")
    list3 = [10, 20, 30]
    value3 = 5
    result3 = check_membership(list3, value3)
    print(f"Is {value3} in {list3}? {result3}")
    empty_list = []
    value4 = 1
    result4 = check_membership(empty_list, value4)
    print(f"Is {value4} in {empty_list}? {result4}")