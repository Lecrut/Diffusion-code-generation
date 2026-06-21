def find_alphabetic_sequences(s):
    sequences = []
    current_sequence = ''
    
    for char in s:
        if char.isalpha():
            current_sequence += char
        else:
            if current_sequence:
                sequences.append(current_sequence)
                current_sequence = ''
    
    if current_sequence:
        sequences.append(current_sequence)
    
    return sequences

if __name__ == '__main__':
    sample_string = "Hello123World!ThisIsAString."
    print(find_alphabetic_sequences(sample_string))