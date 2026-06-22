from itertools import groupby

def compress_string(s: str) -> str:
    if not s:
        return ""
    
    compressed_parts = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        compressed_parts.append(f"{char}{count}")
    
    return "".join(compressed_parts)

if __name__ == "__main__":
    sample_input = "aaabbcdddd"
    result = compress_string(sample_input)
    print(result)
    
    empty_input = ""
    empty_result = compress_string(empty_input)
    print(empty_result)
    
    single_char_input = "z"
    single_result = compress_string(single_char_input)
    print(single_result)