def get_middle_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 0:
        return (sequence[length // 2 - 1], sequence[length // 2])
    else:
        return sequence[length // 2]

if __name__ == '__main__':
    print(get_middle_item([1, 2, 3]))
    print(get_middle_item([1, 2, 3, 4]))
    print(get_middle_item([1]))
    print(get_middle_item([]))
    print(get_middle_item(['a', 'b', 'c', 'd', 'e']))
    print(get_middle_item([10, 20]))