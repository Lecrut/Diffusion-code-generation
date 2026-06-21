def validate_input(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    if len(lst) == 0:
        raise ValueError('The list is empty')

def find_middle_item(lst):
    validate_input(lst)
    n = len(lst)
    middle_index = n // 2
    if n % 2 == 0:
        return (lst[middle_index - 1] + lst[middle_index]) / 2
    else:
        return lst[middle_index]

if __name__ == '__main__':
    sample_list_odd = [3, 1, 4, 1, 5]
    sample_list_even = [2, 7, 1, 8, 2, 8]
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))