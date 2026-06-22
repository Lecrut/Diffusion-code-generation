def get_element(sequence, index):
    return sequence[index]

if __name__ == '__main__':
    sample_sequence = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    target_index = 2
    retrieved_element = get_element(sample_sequence, target_index)
    print(retrieved_element)