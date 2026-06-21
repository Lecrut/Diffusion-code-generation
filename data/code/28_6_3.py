import json
from collections import Counter

def run_length_encode(text: str) -> str:
    if not text:
        return json.dumps([])
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
    return json.dumps(result)

if __name__ == '__main__':
    text = "aabcccccaaa"
    output = run_length_encode(text)
    print(output)