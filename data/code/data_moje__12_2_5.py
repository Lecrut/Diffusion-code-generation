def get_center_item(sequence):
    if not sequence:
        return None
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 1:
        return sequence[mid_index]
    else:
        return (sequence[mid_index - 1], sequence[mid_index])

if __name__ == '__main__':
    print(get_center_item([1, 2, 3]))
    print(get_center_item([1, 2, 3, 4]))
    print(get_center_item([]))
    print(get_center_item([42]))
    print(get_center_item(['a', 'b', 'c', 'd', 'e']))
    print(get_center_item([10, 20]))