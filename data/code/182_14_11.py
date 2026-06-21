from typing import List

def string_to_chars(input_string: str) -> List[str]:
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return list(input_string)

if __name__ == '__main__':
    sample_input = "hello"
    print(string_to_chars(sample_input))