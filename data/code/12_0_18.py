def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence is empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return sequence[length // 2 - 1]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [1, 2, 3, 4, 5, 6]
    sample_single = [42]
    sample_two = [10, 20]
    sample_empty = []

    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))
    print(get_middle_element(sample_single))
    print(get_middle_element(sample_two))
    try:
        get_middle_element(sample_empty)
    except ValueError as e:
        print(str(e))