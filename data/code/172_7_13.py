CODE_TO_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    
    for key, value in data.items():
        if not isinstance(key, int) or not isinstance(value, str):
            raise ValueError("All keys must be integers and all values must be strings")

if __name__ == '__main__':
    validate_input(CODE_TO_WORD)
    print("Code to Word Mapping:")
    for code, word in CODE_TO_WORD.items():
        print(f"{code}: {word}")