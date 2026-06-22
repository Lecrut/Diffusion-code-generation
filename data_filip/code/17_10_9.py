import itertools

def run_length_encode(data: str) -> list[tuple[str, int]]:
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    return result

def run_length_encode_iterator(data: str) -> tuple[str, int]:
    if not data:
        return
    
    grouped_data = itertools.groupby(data)
    
    for key, group in grouped_data:
        count = sum(1 for _ in group)
        yield key, count

def run_length_encode_gentuple(data: str) -> list:
    if not data:
        return []
    
    encoded_list = list(run_length_encode_iterator(data))
    return encoded_list

if __name__ == '__main__':
    sample_input = "aaabbcccccdde"
    encoded_result = run_length_encode_gentuple(sample_input)
    print(encoded_result)