def get_element(sequence, index):
    return sequence[index]

if __name__ == '__main__':
    sample_sequence = ('x', 'y', 'z', 'w', 'v')
    target_index = 1
    retrieved_element = get_element(sample_sequence, target_index)
    print(retrieved_element)