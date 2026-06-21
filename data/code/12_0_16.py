def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise IndexError("Sequence is empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1], sequence[length // 2])

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([10]))
    print(get_middle_element([5, 15]))
    print(get_middle_element([1, 2, 3, 4, 5, 6, 7]))
    print(get_middle_element([10, 20, 30, 40]))