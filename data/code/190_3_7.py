def check_membership(iterable, value):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("The first argument must be a list or tuple.")
    if not isinstance(value, (int, float)):
        raise ValueError("The second argument must be an integer or float.")
    return value in iterable

if __name__ == '__main__':
    list1 = [1.5, 2.3, 3.7, 4.1, 5.9]
    value1 = 3.7
    result1 = check_membership(list1, value1)
    print(f"Is {value1} in {list1}? {result1}")
    
    list2 = [10.2, 20.8, 30.4]
    value2 = 50.5
    result2 = check_membership(list2, value2)
    print(f"Is {value2} in {list2}? {result2}")