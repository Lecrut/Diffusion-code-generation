import sys

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 0
    current_char = text[0]
    
    for char in text:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def run_length_decode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    i = 0
    while i < len(text):
        count_str = ""
        while i < len(text) and text[i].isdigit():
            count_str += text[i]
            i += 1
        if i < len(text):
            char = text[i]
            i += 1
            result.append(char * int(count_str))
    return "".join(result)

if __name__ == "__main__":
    original = "aaabbc"
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)