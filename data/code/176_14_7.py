def find_letter_sequences(s):
    result = set()
    current_sequence = []
    
    for char in s:
        if char.isalpha():
            current_sequence.append(char)
        else:
            if current_sequence:
                result.add(''.join(current_sequence))
                current_sequence = []
    
    if current_sequence:
        result.add(''.join(current_sequence))
    
    return result

if __name__ == '__main__':
    sample_string = "Hello, 世界! Привет!"
    print(find_letter_sequences(sample_string))