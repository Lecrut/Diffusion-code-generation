from typing import List, Tuple

def run_length_encode(s: str) -> List[Tuple[str, int]]:
    if not s:
        return []
    result: List[Tuple[str, int]] = []
    current_char: str = s[0]
    count: int = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_string: str = "aaabbccccd"
    encoded_result: List[Tuple[str, int]] = run_length_encode(sample_string)
    print(encoded_result)