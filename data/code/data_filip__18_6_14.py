from typing import Tuple, List

def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result: List[str] = []
    current_char: str = s[0]
    count: int = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
            
    result.append(f"{count}{current_char}")
    
    return "".join(result)

if __name__ == "__main__":
    sample_text: str = "aaabbbcc"
    encoded: str = run_length_encode(sample_text)
    print(encoded)