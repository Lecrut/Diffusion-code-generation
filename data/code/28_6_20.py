import json

def run_length_encode(text):
    if not text:
        return {}
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append({"char": current_char, "count": count})
            current_char = char
            count = 1
            
    result.append({"char": current_char, "count": count})
    
    return json.dumps(result, separators=(',', ':'))

if __name__ == '__main__':
    sample_string = "aaabbccccdd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)