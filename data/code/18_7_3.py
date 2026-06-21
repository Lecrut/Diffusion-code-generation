def encode_run_length(data: str) -> list[tuple[str, int]]:
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = data[i]
            count = 1
    
    result.append((current_char, count))
    return result

def decode_run_length(encoded_data: list[tuple[str, int]]) -> str:
    result = []
    for char, count in encoded_data:
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = encode_run_length(sample_string)
    print(encoded_result)
    decoded_result = decode_run_length(encoded_result)
    print(decoded_result)