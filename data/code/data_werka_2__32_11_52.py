def calculate_character_count(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    char_count = 0
    for char in input_string:
        char_count += 1
    
    return char_count

if __name__ == '__main__':
    sample_input = "Hello, Alibaba Cloud!"
    character_count = calculate_character_count(sample_input)
    print(character_count)