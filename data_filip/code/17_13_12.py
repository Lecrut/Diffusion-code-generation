def run_length_encode(s: str) -> str:
    if not s:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = s[i]
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        count = int(count_str) if count_str else 1
        char = s[i]
        i += 1
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBC"
    encoded = run_length_encode(sample_input)
    print(encoded)
    
    decoded = run_length_decode(encoded)
    print(decoded)
    
    empty_input = ""
    print(run_length_encode(empty_input))
    
    single_char = "X"
    print(run_length_encode(single_char))
    
    mixed_input = "Hello World!!! 112233"
    encoded_mixed = run_length_encode(mixed_input)
    print(encoded_mixed)
    decoded_mixed = run_length_decode(encoded_mixed)
    print(decoded_mixed)