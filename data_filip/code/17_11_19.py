from typing import List, Tuple

def run_length_encode(data: str) -> List[Tuple[str, int]]:
    if not data:
        return []
    
    encoded: List[Tuple[str, int]] = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = data[i]
            count = 1
            
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded_data: List[Tuple[str, int]]) -> str:
    if not encoded_data:
        return ""
    
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    encoded_result = run_length_encode(sample_string)
    decoded_result = run_length_decode(encoded_result)
    
    print(f"Original: {sample_string}")
    print(f"Encoded: {encoded_result}")
    print(f"Decoded: {decoded_result}")
    print(f"Round-trip match: {sample_string == decoded_result}")