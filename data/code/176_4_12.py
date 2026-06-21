def find_alphabetic_sequences(text):
    sequences = []
    sequence = ''
    for char in text:
        if char.isalpha():
            sequence += char
        elif sequence:
            sequences.append(sequence)
            sequence = ''
    if sequence:
        sequences.append(sequence)
    return sequences
if __name__ == '__main__':
    sample_string = 'Hello, world! This is a test... how are you?'
    result = find_alphabetic_sequences(sample_string)
    print(result)