def run_length_encode(text: str) -> str:
    if not text:
        return ""
    encoded_parts = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded_parts.append(str(count) + current_char)
    return "".join(encoded_parts)

def run_length_decode(encoded_text: str) -> str:
    if not encoded_text:
        return ""
    decoded_parts = []
    i = 0
    while i < len(encoded_text):
        if not encoded_text[i].isdigit():
            raise ValueError(f"Invalid encoding at index {i}")
        count_str = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            count_str += encoded_text[i]
            i += 1
        count = int(count_str)
        if i >= len(encoded_text):
            raise ValueError("Invalid encoding: expected character after count")
        char = encoded_text[i]
        decoded_parts.append(char * count)
        i += 1
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_strings = ["", "a", "aaa", "aabbcccc", "aabbbccccd", "xyz"]
    for s in sample_strings:
        encoded = run_length_encode(s)
        decoded = run_length_decode(encoded)
        print(encoded)
        print(decoded)