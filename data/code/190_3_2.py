def check_membership(iterable, value):
    return value in iterable
if __name__ == '__main__':
    list1 = [1, 5, 8, 10]
    value1 = 8
    result1 = check_membership(list1, value1)
    print(f"Is {value1} in {list1}? {result1}")
    list2 = ['apple', 'banana', 'cherry']
    value2 = 'apple'
    result2 = check_membership(list2, value2)
    print(f"Is {value2} in {list2}? {result2}")
    list3 = [100, 200]
    value3 = 50
    result3 = check_membership(list3, value3)
    print(f"Is {value3} in {list3}? {result3}")