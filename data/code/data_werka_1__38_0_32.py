def find_repeated_letters(input_string):
    repeated_letters = []
    seen_letters = set()
    
    for char in input_string:
        if char.isalpha() and char.lower() in seen_letters:
            if char not in repeated_letters:
                repeated_letters.append(char)
        else:
            seen_letters.add(char.lower())
    
    return repeated_letters

if __name__ == '__main__':
    sample_input = "This is a simple test string."
    result = find_repeated_letters(sample_input)
    print(result)