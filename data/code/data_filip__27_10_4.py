def run_length_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(text: str) -> str:
    if not text:
        return ""
    result = []
    i = 0
    while i < len(text):
        count_str = []
        while i < len(text) and text[i].isdigit():
            count_str.append(text[i])
            i += 1
        if not count_str:
            raise ValueError("Invalid encoding: expected a digit")
        count = int("".join(count_str))
        if i >= len(text):
            raise ValueError("Invalid encoding: expected a character after count")
        char = text[i]
        i += 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    original_string = "aabcccccaaa"
    encoded = run_length_encode(original_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    print(original_string == decoded)