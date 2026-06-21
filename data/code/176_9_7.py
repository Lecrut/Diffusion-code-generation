def find_letter_sequences(text):
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
    sample_text = "Hello, World! 123 Python 3.8"
    print(find_letter_sequences(sample_text))