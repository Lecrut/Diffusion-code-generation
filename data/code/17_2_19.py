def extract_final_entry(sequence):
    if not sequence:
        raise IndexError("sequence is empty")
    length = len(sequence)
    return sequence[length - 1]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = extract_final_entry(sample_tuple)
    print(result)