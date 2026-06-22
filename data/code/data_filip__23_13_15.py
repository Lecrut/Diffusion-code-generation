def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    count = 1
    length = len(text)
    
    for i in range(1, length):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{text[i - 1]}")
            count = 1
    encoded.append(f"{count}{text[-1]}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = run_length_encode(sample_string)
    print(result)