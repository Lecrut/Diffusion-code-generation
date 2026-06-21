def find_alphabetic_sequences(text):
    sequences = []
    current_sequence = ""
    
    for char in text:
        if char.isalpha():
            current_sequence += char
        else:
            if current_sequence:
                sequences.append(current_sequence)
                current_sequence = ""
    
    if current_sequence:
        sequences.append(current_sequence)
    
    return sequences

if __name__ == '__main__':
    sample_string = "Hello, world! 123 This is a test... how are you?"
    result = find_alphabetic_sequences(sample_string)
    print(result)