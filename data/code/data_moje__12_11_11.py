def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    return sequence[length // 2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(get_middle_element(sample_tuple))
    try:
        get_middle_element(())
    except ValueError as e:
        print(e)