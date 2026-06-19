def get_element(sequence, index):
    return sequence[index]

if __name__ == '__main__':
    sample_sequence = (10, 20, 30, 40, 50)
    sample_index = 2
    result = get_element(sample_sequence, sample_index)
    print(result)