def calculate_character_count(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return len(input_string)

if __name__ == '__main__':
    sample_inputs = {
        "Hello, World!": 13,
        "Python": 6,
        "": 0,
        "OpenAI": 6,
        "ChatGPT": 7
    }
    
    for input_str, expected_count in sample_inputs.items():
        character_count = calculate_character_count(input_str)
        print(f"Input: '{input_str}' | Expected Count: {expected_count} | Calculated Count: {character_count}")