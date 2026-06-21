def get_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("The sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    print(get_first_element(sample_list))

    sample_empty_list = []
    try:
        print(get_first_element(sample_empty_list))
    except IndexError:
        print("IndexError raised correctly")