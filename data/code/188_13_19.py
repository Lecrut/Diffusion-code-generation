def reverse_list(iterable):
    if not isinstance(iterable, list):
        raise ValueError('Input must be a list')
    return iterable[::-1]
if __name__ == '__main__':
    try:
        list1 = [1, 2, 3, 4, 5]
        print(f'Original: {list1}, Reversed: {reverse_list(list1)}')
        list2 = ['a', 'b', 'c']
        print(f'Original: {list2}, Reversed: {reverse_list(list2)}')
        empty_list = []
        print(f'Original: {empty_list}, Reversed: {reverse_list(empty_list)}')
        list3 = [10]
        print(f'Original: {list3}, Reversed: {reverse_list(list3)}')
        invalid_input = 'not a list'
        reverse_list(invalid_input)
    except ValueError as e:
        print(e)