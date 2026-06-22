def compress_string(input_string: str) -> str:
    if not input_string:
        return ""
    
    compressed_chars: list[str] = []
    count: int = 1
    length: int = len(input_string)
    
    for i in range(1, length):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed_chars.append(input_string[i - 1])
            compressed_chars.append(str(count))
            count = 1
    
    compressed_chars.append(input_string[-1])
    compressed_chars.append(str(count))
    
    compressed_str: str = "".join(compressed_chars)
    
    if len(compressed_str) < len(input_string):
        return compressed_str
    else:
        return input_string

if __name__ == '__main__':
    original = 'aabcccccaaa'
    result = compress_string(original)
    print(result)