def find_alphabetic_sequences(text):
    SEPARATORS = '.,?!;:"\'()[]{}'
    sequences = []
    current_sequence = []

    for char in text:
        if char not in SEPARATORS:
            current_sequence.append(char)
        else:
            if current_sequence:
                sequences.append(''.join(current_sequence))
                current_sequence = []

    if current_sequence:
        sequences.append(''.join(current_sequence))

    return sequences

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test... how are you?"
    result = find_alphabetic_sequences(sample_string)
    print(result)