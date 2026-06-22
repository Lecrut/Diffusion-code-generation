import re

def run_length_encode(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    pattern = re.compile(r'(.)\1*')
    for match in pattern.finditer(input_string):
        char = match.group(1)
        length = len(match.group(0))
        encoded_parts.append(f"{char}{length}")
    
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_data = "aaabbccccd"
    result = run_length_encode(sample_data)
    print(result)