def locate_center_item(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    count = len(sequence)
    is_odd = count % 2 != 0
    if is_odd:
        center_index = count // 2
    else:
        center_index = (count // 2) - 1
    return sequence[center_index]

if __name__ == '__main__':
    numbers = [15, 25, 35, 45, 55, 65, 75]
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    single_item = [99]
    print(locate_center_item(numbers))
    print(locate_center_item(letters))
    print(locate_center_item(single_item))
    print(locate_center_item([100, 200]))