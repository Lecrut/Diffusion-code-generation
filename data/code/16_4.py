def get_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first_element(sample_list)
    print(result)
    sample_tuple = ()
    try:
        get_first_element(sample_tuple)
    except IndexError as e:
        print(e)