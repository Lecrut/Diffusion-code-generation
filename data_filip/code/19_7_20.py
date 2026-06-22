def compress_run_length(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(f"{count}{s[i-1]}")
            count = 1
    result.append(f"{count}{s[-1]}")
    return "".join(result)

def decompress_run_length(s):
    if not s:
        return ""
    result = []
    i = 0
    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        if i < len(s):
            char = s[i]
            count = int(count_str) if count_str else 1
            result.append(char * count)
            i += 1
    return "".join(result)

def bidirectional_rle_verify(input_string):
    compressed = compress_run_length(input_string)
    decompressed = decompress_run_length(compressed)
    return {
        "original": input_string,
        "compressed": compressed,
        "decompressed": decompressed,
        "integrity_check": input_string == decompressed
    }

if __name__ == '__main__':
    sample_data = "AAABBBCCDDEEEEE"
    result = bidirectional_rle_verify(sample_data)
    print(result)