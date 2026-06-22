def retrieve_second_element(seq):
    return seq[1] if len(seq) > 1 else None

if __name__ == '__main__':
    test_sequence = [9, 18, 27, 36, 45]
    second_element = retrieve_second_element(test_sequence)
    print(second_element)