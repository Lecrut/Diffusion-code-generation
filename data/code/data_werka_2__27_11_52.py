def values_differ(a, b):
    return not (a == b)

if __name__ == '__main__':
    first_value = 5
    second_value = '5'
    print(values_differ(first_value, second_value))

    third_value = [1, 2, 3]
    fourth_value = [1, 2, 3]
    print(values_differ(third_value, fourth_value))

    fifth_value = {'key': 'value'}
    sixth_value = {'key': 'value'}
    print(values_differ(fifth_value, sixth_value))