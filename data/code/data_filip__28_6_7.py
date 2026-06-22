import json
from collections import defaultdict

def run_length_encode(text: str) -> str:
    if not text:
        return json.dumps([])
    
    encoded = []
    count = 0
    current_char = text[0]
    
    for char in text:
        if char == current_char:
            count += 1
        else:
            encoded.append([current_char, count])
            current_char = char
            count = 1
    encoded.append([current_char, count])
    
    return json.dumps(encoded)

if __name__ == '__main__':
    sample_string = "aaabbbcccc"
    result = run_length_encode(sample_string)
    print(result)