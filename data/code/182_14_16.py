from typing import List

def validate_input(input_string: str) -> None:
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def string_to_chars(input_string: str) -> List[str]:
    validate_input(input_string)
    return list(input_string)

if __name__ == '__main__':
    sample_input = "hello"
    char_list = string_to_chars(sample_input)
    print(char_list)