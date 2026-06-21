def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def calculate_character_count(input_string):
    validate_input(input_string)
    return len(input_string)

if __name__ == '__main__':
    sample_inputs = [
        "Hello, World!",
        "Python",
        "",
        "OpenAI",
        "ChatGPT"
    ]
    
    for input_str in sample_inputs:
        character_count = calculate_character_count(input_str)
        print(f"'{input_str}' has {character_count} characters.")