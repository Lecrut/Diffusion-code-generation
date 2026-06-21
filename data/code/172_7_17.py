def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    for key, value in data.items():
        if not isinstance(key, int) or not isinstance(value, str):
            raise ValueError("All keys must be integers and all values must be strings")

CODE_TO_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

def get_code_to_word_mapping():
    validate_input(CODE_TO_WORD)
    return CODE_TO_WORD

if __name__ == '__main__':
    sample_mapping = get_code_to_word_mapping()
    print("Sample Code to Word Mapping:")
    for code, word in sample_mapping.items():
        print(f"{code}: {word}")