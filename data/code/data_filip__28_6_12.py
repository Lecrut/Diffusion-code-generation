import json

def run_length_encode(text):
    if not text:
        return []
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append({"char": current_char, "count": count})
            current_char = text[i]
            count = 1
    result.append({"char": current_char, "count": count})
    return json.dumps(result, separators=(',', ':'))

if __name__ == '__main__':
    sample_string = "aaabbbccccdd"
    print(run_length_encode(sample_string))