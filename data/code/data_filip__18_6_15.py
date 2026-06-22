from typing import List, Tuple, Optional

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result: List[str] = []
    count: int = 1
    current_char: str = text[0]
    
    for i in range(1, len(text)):
        char: str = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string: str = "aaabbccccd"
    encoded_result: str = run_length_encode(sample_string)
    print(encoded_result)