def find_repeated_letters(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    REPEAT_THRESHOLD = 1
    letter_counts = {}
    
    for char in input_string:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in letter_counts:
                letter_counts[lower_char] += 1
            else:
                letter_counts[lower_char] = 1
    
    repeated_letters = [letter for letter, count in letter_counts.items() if count > REPEAT_THRESHOLD]
    
    return repeated_letters

if __name__ == '__main__':
    sample_input = "This is a simple test string with some repeated letters."
    result = find_repeated_letters(sample_input)
    print(result)