def values_differ(a, b):
    return not a == b

if __name__ == '__main__':
    first_value = 7
    second_value = 'seven'
    print(values_differ(first_value, second_value))

    list1 = [3, 4, 5]
    list2 = [3, 4, 5]
    print(values_differ(list1, list2))

    dict1 = {'key': 'value'}
    dict2 = {'key': 'different value'}
    print(values_differ(dict1, dict2))