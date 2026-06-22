import json

def run_length_encode(text: str) -> str:
    if not text:
        return json.dumps([])
    encoded_list = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_list.append([current_char, count])
            current_char = char
            count = 1
    encoded_list.append([current_char, count])
    return json.dumps(encoded_list)

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = run_length_encode(sample_string)
    print(result)