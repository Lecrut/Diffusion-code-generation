def extract_second_element(sequence):
    index_map = {'second': 1}
    return sequence[index_map['second']]

if __name__ == '__main__':
    example_sequence = [5, 15, 25, 35, 45]
    second_element = extract_second_element(example_sequence)
    print(second_element)