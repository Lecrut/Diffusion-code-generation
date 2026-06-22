def _validate_list_for_second_to_last(lst):
    if not isinstance(lst, (list, tuple)):
        raise TypeError("Input must be a sequence type")
    if len(lst) < 2:
        raise IndexError("List must contain at least two elements")

def retrieve_second_to_last(sequence):
    _validate_list_for_second_to_last(sequence)
    return sequence[-2]

if __name__ == '__main__':
    data = [1, 3, 5, 7, 9, 11]
    val = retrieve_second_to_last(data)
    print(val)