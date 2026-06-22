import re

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    result = []
    last_char = text[0]
    count = 1
    for char in text[1:]:
        if char == last_char:
            count += 1
        else:
            result.append(f"{count}{last_char}")
            last_char = char
            count = 1
    result.append(f"{count}{last_char}")
    return "".join(result)

if __name__ == '__main__':
    input_string = "aaabbbcccddeefffffghijklmnopqrstuvwxyz"
    encoded_result = run_length_encode(input_string)
    print(encoded_result)