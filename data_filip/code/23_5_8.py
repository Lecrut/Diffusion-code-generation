def run_length_encode(s: str) -> str:
    if s is None:
        raise TypeError("Input must be a string.")
    
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
        
    if len(s) == 0:
        return ""

    encoded = []
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_text = "aaabbc"
    result = run_length_encode(sample_text)
    print(result)