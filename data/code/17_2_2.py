def extract_last_entry(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    index = len(sequence) - 1
    return sequence[index]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = extract_last_entry(sample_tuple)
    print(result)