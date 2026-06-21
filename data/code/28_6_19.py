import json

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append([count, current_char])
            current_char = char
            count = 1
    encoded.append([count, current_char])
    return encoded

if __name__ == '__main__':
    sample_string = "AAABBC"
    result = run_length_encode(sample_string)
    print(json.dumps(result))