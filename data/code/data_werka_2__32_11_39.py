CHARACTER_COUNT_CONSTANT = 1

def calculate_character_count(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string) * CHARACTER_COUNT_CONSTANT

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    character_count = calculate_character_count(sample_input)
    print(character_count)