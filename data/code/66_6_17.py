def is_number(value):
    return isinstance(value, (int, float))

def validate_adjacent_numbers(data):
    for i in range(len(data) - 1):
        if not is_number(data[i]) or not is_number(data[i + 1]):
            raise TypeError(f'Non-numeric elements found: {data[i]} and {data[i + 1]}')

def is_sorted(data):
    validate_adjacent_numbers(data)
    n = len(data)
    if n <= 1:
        return True
    for i in range(n - 1):
        if data[i] > data[i + 1]:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1.5, 2.5, 3.5, 4.5, 5.5]
    list3 = ['a', 2, 3, 4, 5]
    list4 = [1, 1, 2, 3, 3]
    list5 = [10]
    list6 = []
    try:
        print(f'List 1 is sorted: {is_sorted(list1)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 2 is sorted: {is_sorted(list2)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 3 is sorted: {is_sorted(list3)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 4 is sorted: {is_sorted(list4)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 5 is sorted: {is_sorted(list5)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 6 is sorted: {is_sorted(list6)}')
    except TypeError as e:
        print(e)