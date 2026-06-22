from typing import List, Tuple

def run_length_encode(data: str) -> str:
    if not data:
        return ""
    
    result: List[str] = []
    count: int = 1
    current_char: str = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_string: str = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_string: str = run_length_encode(sample_string)
    print(encoded_string)