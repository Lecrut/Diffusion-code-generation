import json

def run_length_encode(s):
    if not s:
        return []
    encoded = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append({"character": current_char, "count": count})
            current_char = s[i]
            count = 1
    encoded.append({"character": current_char, "count": count})
    return encoded

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    result = run_length_encode(sample_string)
    print(json.dumps(result))