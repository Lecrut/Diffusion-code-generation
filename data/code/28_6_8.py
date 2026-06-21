import json

def run_length_encode(s):
    if not s:
        return ""
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append({"char": current_char, "count": count})
            current_char = char
            count = 1
    result.append({"char": current_char, "count": count})
    return json.dumps(result, separators=(',', ':'))

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    print(run_length_encode(sample_string))