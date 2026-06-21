import re

def decode_rle(rle_string):
    if not isinstance(rle_string, str):
        raise TypeError("Input must be a string")
    
    if not rle_string:
        return ""
    
    pattern = re.compile(r'(?!^)(\d+)([A-Za-z])|([A-Za-z])')
    matches = pattern.findall(rle_string)
    
    result = []
    for match in matches:
        if match[0] and match[1]:
            count = int(match[0])
            char = match[1]
            result.append(char * count)
        elif match[2]:
            char = match[2]
            result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    test_cases = [
        "A2B3C",
        "12X5Y",
        "ABC",
        "1A2B3C",
        "23A45B",
        "",
        "10Z",
        "A",
        "100a"
    ]
    
    for test in test_cases:
        decoded = decode_rle(test)
        print(decoded)