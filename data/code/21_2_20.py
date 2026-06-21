from typing import List, Tuple, Any

def rle_encode(sequence: str) -> List[Tuple[str, int]]:
    if not sequence:
        return []

    encoded = []
    current_char = sequence[0]
    current_count = 1
    iterator = iter(sequence)

    for char in iterator:
        if char == current_char:
            current_count += 1
        else:
            encoded.append((current_char, current_count))
            current_char = char
            current_count = 1

    encoded.append((current_char, current_count))
    return encoded

if __name__ == '__main__':
    sample_text = "aaabbc"
    result = rle_encode(sample_text)
    print(result)