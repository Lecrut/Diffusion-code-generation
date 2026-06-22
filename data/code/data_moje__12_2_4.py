def get_central_item(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    if length % 2 == 0:
        raise ValueError("Sequence has even length, no single central item")
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_odd_list = [1, 2, 3, 4, 5]
    sample_odd_string = "abcde"
    sample_tuple = (10, 20, 30, 40, 50)

    print(get_central_item(sample_odd_list))
    print(get_central_item(sample_odd_string))
    print(get_central_item(sample_tuple))

    try:
        get_central_item([1, 2, 3, 4])
    except ValueError as e:
        print(str(e))

    try:
        get_central_item([])
    except ValueError as e:
        print(str(e))