import re

def clean_and_verify(input_string: str) -> int:
    if input_string is None:
        raise ValueError("Input cannot be None")
    
    remove_chars = "".join([chr(i) for i in range(256) if not chr(i).isdigit() and chr(i) != '-'])
    table = str.maketrans("", "", remove_chars)
    
    cleaned_string = input_string.translate(table)
    
    if not cleaned_string or cleaned_string == '-':
        raise ValueError("Remaining string does not consist solely of integers")
        
    if len(cleaned_string) > 1 and cleaned_string.startswith('-'):
        cleaned_string = cleaned_string[1:]
        if not cleaned_string:
            raise ValueError("Remaining string does not consist solely of integers")

    try:
        value = int(cleaned_string)
    except ValueError:
        raise ValueError("Remaining string does not consist solely of integers")
        
    return value

if __name__ == '__main__':
    sample_texts = ["  -123  ", "abc123xyz", "  456  ", "--789"]
    
    for text in sample_texts:
        try:
            result = clean_and_verify(text)
            print(result)
        except ValueError:
            print(f"Failed to parse '{text}'")