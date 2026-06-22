import re

def isolate_punctuation(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    punctuation_pattern = r'([^\w\s])'
    isolated_text = re.sub(punctuation_pattern, r'\1 ', input_string)
    return isolated_text

if __name__ == '__main__':
    sample_input = "Hello, world! How are you?"
    print(isolate_punctuation(sample_input))