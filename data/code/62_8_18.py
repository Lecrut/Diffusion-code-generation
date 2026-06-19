def retrieve_second_element(sequence):
    SECOND_INDEX = 1
    return sequence[SECOND_INDEX]

if __name__ == '__main__':
    demonstration_sequence = [9, 18, 27, 36, 45]
    second_value = retrieve_second_element(demonstration_sequence)
    print(second_value)