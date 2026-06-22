from typing import List, Tuple

def group_runs(text: str) -> List[Tuple[str, int]]:
    if not text:
        return []
    
    groups: List[Tuple[str, int]] = []
    current_char = text[0]
    count = 1
    
    for index in range(1, len(text)):
        if text[index] == current_char:
            count += 1
        else:
            groups.append((current_char, count))
            current_char = text[index]
            count = 1
    groups.append((current_char, count))
    return groups

def run_length_encode(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    groups = group_runs(text)
    encoded_parts = []
    for char, count in groups:
        encoded_parts.append(f"{char}{count}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_data = 'aaabbbccc'
    result = run_length_encode(sample_data)
    print(result)