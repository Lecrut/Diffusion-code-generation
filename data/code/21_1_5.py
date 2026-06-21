import unittest

def run_length_encode(data):
    if not data:
        return ""
    
    encoded = []
    count = 1
    current_char = data[0]
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = data[i]
            count = 1
            
    encoded.append(str(count) + current_char)
    
    return "".join(encoded)

def run_length_decode(data):
    if not data:
        return ""
    
    decoded = []
    i = 0
    
    while i < len(data):
        count_str = []
        while i < len(data) and data[i].isdigit():
            count_str.append(data[i])
            i += 1
        
        count = int("".join(count_str))
        char = data[i]
        decoded.append(char * count)
        i += 1
        
    return "".join(decoded)

if __name__ == '__main__':
    test_cases = [
        ("", ""),
        ("A", "1A"),
        ("AA", "2A"),
        ("AAB", "2A1B"),
        ("ABC", "1A1B1C"),
        ("AABBCCC", "2A2B3C"),
        ("XYZ", "1X1Y1Z"),
    ]
    
    results = {}
    for input_val, expected in test_cases:
        encoded = run_length_encode(input_val)
        decoded = run_length_decode(encoded)
        is_correct = encoded == expected and decoded == input_val
        results[f"{repr(input_val)} -> {repr(encoded)}"] = is_correct
    
    print(results)