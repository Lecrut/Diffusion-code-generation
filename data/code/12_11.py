def get_middle_element(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    return sequence[len(sequence) // 2]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(get_middle_element(sample_tuple))
    empty_tuple = ()
    try:
        print(get_middle_element(empty_tuple))
    except ValueError as e:
        print(e)