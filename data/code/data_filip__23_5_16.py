def compress_rle(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        return ""
    
    result = []
    current_char = s[0]
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = ["AABCCCAA", "ABCDE", "AAAA", "A", ""]
    for sample in sample_inputs:
        result = compress_rle(sample)
        print(f"Input: {sample!r} -> Output: {result!r}")
    
    try:
        compress_rle(None)
    except TypeError as e:
        print(f"Caught expected error: {e}")