def get_second_last_element(sequence):
    if len(sequence) < 2:
        raise IndexError("List must have at least two elements")
    index_map = {
        'first': 0,
        'last': -1,
        'second_last': -2
    }
    return sequence[index_map['second_last']]

if __name__ == '__main__':
    sample_integers = [1, 2, 3, 4, 5]
    result_value = get_second_last_element(sample_integers)
    print(result_value)