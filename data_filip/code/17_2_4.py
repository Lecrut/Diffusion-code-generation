import itertools

def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed_parts = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        compressed_parts.append(f"{count}{char}")
    
    return "".join(compressed_parts)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = compress_string(sample_input)
    print(result)