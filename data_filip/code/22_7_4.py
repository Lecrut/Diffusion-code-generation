import sys

def decode_rle(compressed: str) -> str:
    if not compressed:
        return ""
    
    result = []
    i = 0
    n = len(compressed)
    
    while i < n:
        char = compressed[i]
        i += 1
        
        if i >= n:
            result.append(char)
            break
        
        count_str = []
        while i < n and compressed[i].isdigit():
            count_str.append(compressed[i])
            i += 1
        
        if count_str:
            count = int("".join(count_str))
            result.append(char * count)
        else:
            result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "a3b2c1",
        "12a3b2",
        "z9x1y0",
        "hello5",
        "a1b2c3d4e5",
        "100a"
    ]
    
    for test in test_cases:
        print(f"Input: {test} -> Output: {decode_rle(test)}")