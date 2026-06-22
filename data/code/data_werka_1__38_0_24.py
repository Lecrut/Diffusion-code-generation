def find_repeated_letters(input_string):
    repeated_letters = set()
    seen_letters = set()
    
    for char in input_string:
        if char.isalpha() and char.lower() in seen_letters:
            repeated_letters.add(char.lower())
        else:
            seen_letters.add(char.lower())
    
    return list(repeated_letters)

if __name__ == '__main__':
    sample_input = "Programming"
    result = find_repeated_letters(sample_input)
    print(result)