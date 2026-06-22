import itertools
import re

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    groups = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        if count == 1:
            groups.append(char)
        else:
            groups.append(f"{count}{char}")
    
    return "".join(groups)

def run_length_decode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    count = 0
    
    for char in text:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            if count > 0:
                result.append(char * count)
                count = 0
            else:
                result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    original = "aabcccccaaa"
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)