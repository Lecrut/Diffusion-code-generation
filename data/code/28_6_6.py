import json

def run_length_encode(s):
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append([current_char, count])
            current_char = s[i]
            count = 1
    result.append([current_char, count])
    return result

if __name__ == '__main__':
    sample_string = "aaabbccccddee"
    encoded_data = run_length_encode(sample_string)
    json_output = json.dumps(encoded_data)
    print(json_output)