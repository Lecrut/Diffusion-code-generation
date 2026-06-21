from typing import List, Tuple

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded_parts: List[str] = []
    current_char: str = text[0]
    count: int = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    encoded_parts.append(f"{current_char}{count}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input: str = "aaabbccccd"
    result: str = run_length_encode(sample_input)
    print(result)