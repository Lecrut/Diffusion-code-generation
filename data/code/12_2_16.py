def get_middle_item(sequence):
    length = len(sequence)
    if length == 0:
        return None
    middle_index = length // 2
    if length % 2 == 1:
        return sequence[middle_index]
    else:
        return (sequence[middle_index - 1], sequence[middle_index])

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [1, 2, 3, 4]
    sample3 = [42]
    sample4 = []

    print(get_middle_item(sample1))
    print(get_middle_item(sample2))
    print(get_middle_item(sample3))
    print(get_middle_item(sample4))