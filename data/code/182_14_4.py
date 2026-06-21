from typing import List

def string_to_chars(input_string: str) -> List[str]:
    return list(input_string)

if __name__ == '__main__':
    sample_input = "python"
    char_list = string_to_chars(sample_input)
    print(char_list)