def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    encoded = []
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(current_char)
            current_char = text[i]
            count = 1
    
    encoded.append(str(count))
    encoded.append(current_char)
    
    return "".join(encoded)

if __name__ == '__main__':
    test_cases = [
        ("AAABBBCCCA", "3A3B3C1A"),
        ("XYZ", "1X1Y1Z"),
        ("A", "1A"),
        ("", "")
    ]
    
    results = {}
    for input_str, expected in test_cases:
        result = run_length_encode(input_str)
        results[f"encode({repr(input_str)})"] = result
    
    for key, value in results.items():
        print(f"{key}: {value}")