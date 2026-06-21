def is_alphabetic(char):
    return 'a' <= char.lower() <= 'z'

def extract_sequences(text):
    sequences = []
    current_sequence = ''
    for char in text:
        if is_alphabetic(char):
            current_sequence += char
        elif current_sequence:
            sequences.append(current_sequence)
            current_sequence = ''
    if current_sequence:
        sequences.append(current_sequence)
    return sequences
if __name__ == '__main__':
    sample_string = 'Hello, world! This is a test... how are you?'
    result = extract_sequences(sample_string)
    print(result)