def extract_alphabetic_sequences(text):
    sequences = []
    current_sequence = ''
    
    for char in text:
        if char.isalpha():
            current_sequence += char
        elif current_sequence:
            sequences.append(current_sequence)
            current_sequence = ''
    
    if current_sequence:
        sequences.append(current_sequence)
    
    return sequences

if __name__ == '__main__':
    sample_string = "Hello, world! 123 This is a test... how are you?"
    result = extract_alphabetic_sequences(sample_string)
    print(result)