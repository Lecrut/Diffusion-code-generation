def compare_adjacent_numbers(data):
    if not data:
        return True
    previous = data[0]
    if not isinstance(previous, (int, float)):
        raise TypeError(f'First element {previous} is not a number')
    for current in data[1:]:
        if not isinstance(current, (int, float)):
            raise TypeError(f'Element {current} is not a number')
        if previous > current:
            return False
        previous = current
    return True
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 3, 2, 4, 5]
    list3 = ['a', 4, 3, 2, 1]
    list4 = [10]
    list5 = []
    list6 = [1.5, 2.5, 3.5]
    try:
        print(f'List 1 is sorted: {compare_adjacent_numbers(list1)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 2 is sorted: {compare_adjacent_numbers(list2)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 3 is sorted: {compare_adjacent_numbers(list3)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 4 is sorted: {compare_adjacent_numbers(list4)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 5 is sorted: {compare_adjacent_numbers(list5)}')
    except TypeError as e:
        print(e)
    try:
        print(f'List 6 is sorted: {compare_adjacent_numbers(list6)}')
    except TypeError as e:
        print(e)