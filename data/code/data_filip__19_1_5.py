import re

def decode_rle(encoded):
    if not isinstance(encoded, str):
        raise ValueError("Input must be a string")
    pattern = r'(\d+)([a-zA-Z0-9_\-\.\!\@\#\$\%\^\&\*\(\)\=\+\[\]\{\}\<\>\?\/\,;\'\"\\~\s])'
    matches = re.findall(pattern, encoded)
    result = []
    for count, char in matches:
        result.append(char * int(count))
    return ''.join(result)

if __name__ == '__main__':
    sample1 = "3A2B5C"
    sample2 = "12X1Y"
    sample3 = "0Z"
    sample4 = "2_3-"
    sample5 = ""
    
    print(decode_rle(sample1))
    print(decode_rle(sample2))
    print(decode_rle(sample3))
    print(decode_rle(sample4))
    print(decode_rle(sample5))