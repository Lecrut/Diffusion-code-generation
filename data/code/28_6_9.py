import json
import re

def rle_encode(text):
    if not text:
        return []
    result = []
    pattern = re.compile(r'(.)\1*')
    for match in pattern.finditer(text):
        char = match.group(1)
        count = len(match.group(0))
        result.append({"char": char, "count": count})
    return result

def rle_encode_to_json(text):
    encoded_list = rle_encode(text)
    return json.dumps(encoded_list)

if __name__ == '__main__':
    sample_text = "aaabbbccc"
    output = rle_encode_to_json(sample_text)
    print(output)