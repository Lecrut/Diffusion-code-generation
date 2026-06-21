def get_middle_element(sequence):
    if not sequence:
        raise ValueError('Sequence is empty')
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        mid_index = mid_index - 1
    return sequence[mid_index]
if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([1]))
    print(get_middle_element([1, 2]))
    print(get_middle_element('abc'))
    print(get_middle_element('abcd'))
    print(get_middle_element((1, 2, 3)))
    print(get_middle_element((1, 2, 3, 4)))
    print(get_middle_element([42]))
    print(get_middle_element([]))