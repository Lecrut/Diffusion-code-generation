def find_letter_sequences(s):
    sequences = set()
    current_sequence = ""
    
    for char in s:
        if char.isalpha():
            current_sequence += char
        else:
            if current_sequence:
                sequences.add(current_sequence)
                current_sequence = ""
    
    if current_sequence:
        sequences.add(current_sequence)
    
    return sequences

if __name__ == '__main__':
    sample_string = "Hello, 世界! Привет, мир!"
    result = find_letter_sequences(sample_string)
    print(result)