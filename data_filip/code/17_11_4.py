from typing import List, Tuple

def run_length_encode(s: str) -> List[Tuple[str, int]]:
    if not s:
        return []

    encoded_data: List[Tuple[str, int]] = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_data.append((current_char, count))
            current_char = char
            count = 1

    encoded_data.append((current_char, count))
    return encoded_data

if __name__ == '__main__':
    sample_string = "aaabbccccd"
    result = run_length_encode(sample_string)
    print(result)