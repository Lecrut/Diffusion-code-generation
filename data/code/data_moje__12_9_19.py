def get_middle(sequence):
    n = len(sequence)
    if n == 0:
        raise IndexError("Cannot get middle item of an empty sequence")
    middle_index = n // 2
    if n % 2 == 1:
        return sequence[middle_index]
    else:
        left_item = sequence[middle_index - 1]
        right_item = sequence[middle_index]
        if left_item == right_item:
            return left_item
        return [left_item, right_item]

if __name__ == '__main__':
    print(get_middle([1, 2, 3, 4, 5]))
    print(get_middle([1, 2, 3, 4]))
    print(get_middle([10]))
    print(get_middle([10, 20]))
    print(get_middle([1, 3, 5, 7, 9, 11, 13]))
    print(get_middle([1, 2, 3, 4, 5, 6]))