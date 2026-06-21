def calculate_character_count(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    character_count = 0
    for char in input_string:
        character_count += 1
    
    return character_count

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    result = calculate_character_count(sample_input)
    print(result)