def is_valid_string(s):
    return isinstance(s, str)

def find_repeated_letters(input_string):
    if not is_valid_string(input_string):
        raise ValueError("Input must be a string")
    
    repeated_letters = []
    seen_letters = set()
    
    for letter in input_string:
        lower_letter = letter.lower()
        if lower_letter.isalpha():
            if lower_letter in seen_letters and lower_letter not in repeated_letters:
                repeated_letters.append(lower_letter)
            else:
                seen_letters.add(lower_letter)
    
    return repeated_letters

if __name__ == '__main__':
    sample_input = "Alibaba Cloud is a great platform for developers."
    result = find_repeated_letters(sample_input)
    print(result)