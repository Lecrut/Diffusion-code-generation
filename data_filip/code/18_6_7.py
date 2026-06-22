from typing import List, Tuple

def run_length_encode(input_string: str) -> str:
    if not input_string:
        return ""
    
    result: List[str] = []
    current_char: str = input_string[0]
    count: int = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = input_string[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_data: str = "aaabbccccdd"
    encoded_result: str = run_length_encode(sample_data)
    print(encoded_result)