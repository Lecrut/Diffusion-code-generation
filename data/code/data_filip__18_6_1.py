from typing import List, Tuple

def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    encoded_parts: List[str] = []
    current_char: str = input_string[0]
    count: int = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_parts.append(str(count) + current_char)
            current_char = input_string[i]
            count = 1
    
    encoded_parts.append(str(count) + current_char)
    
    return "".join(encoded_parts)

if __name__ == "__main__":
    sample_data: str = "aaabbccccd"
    result: str = run_length_encode(sample_data)
    print(result)