from typing import List, Tuple, Optional

def run_length_encode(text: str) -> List[Tuple[str, int]]:
    if not text:
        return []

    encoded_data: List[Tuple[str, int]] = []
    current_char = text[0]
    count = 1

    for index in range(1, len(text)):
        if text[index] == current_char:
            count += 1
        else:
            encoded_data.append((current_char, count))
            current_char = text[index]
            count = 1

    encoded_data.append((current_char, count))
    return encoded_data

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result = run_length_encode(sample_string)
    print(result)