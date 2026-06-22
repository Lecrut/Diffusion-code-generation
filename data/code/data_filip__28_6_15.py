import json

def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append({"char": current_char, "count": count})
            current_char = char
            count = 1
    encoded.append({"char": current_char, "count": count})
    return json.dumps(encoded)

if __name__ == '__main__':
    result = run_length_encode("AAABBBCC")
    print(result)