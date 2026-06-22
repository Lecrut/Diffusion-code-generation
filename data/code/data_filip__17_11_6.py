from typing import List, Tuple, Any

def run_length_encode(data: Any) -> List[Tuple[Any, int]]:
    if not data:
        return []

    encoded_list: List[Tuple[Any, int]] = []
    current_value = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_value:
            count += 1
        else:
            encoded_list.append((current_value, count))
            current_value = data[i]
            count = 1

    encoded_list.append((current_value, count))

    return encoded_list

if __name__ == '__main__':
    sample_string = "AAABBBCCDA"
    result = run_length_encode(sample_string)
    print(result)