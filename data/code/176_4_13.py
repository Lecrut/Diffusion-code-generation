def find_alphabetic_sequences(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    sequences = []
    current_sequence = ""
    
    for char in text:
        if char.isalpha():
            current_sequence += char
        elif current_sequence:
            sequences.append(current_sequence)
            current_sequence = ""
    
    if current_sequence:
        sequences.append(current_sequence)
    
    return sequences

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test... how are you?"
    result = find_alphabetic_sequences(sample_string)
    print(result)