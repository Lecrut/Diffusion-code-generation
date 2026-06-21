import re

def check_run_length_compression(original: str) -> float:
    if not original:
        return 0.0
    
    encoded = ""
    if original:
        count = 1
        last_char = original[0]
        for char in original[1:]:
            if char == last_char:
                count += 1
            else:
                encoded += f"{last_char}{count}"
                last_char = char
                count = 1
        encoded += f"{last_char}{count}"
    
    original_len = len(original)
    compressed_len = len(encoded)
    
    if original_len == 0:
        return 0.0
    
    ratio = compressed_len / original_len
    return ratio

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = check_run_length_compression(sample_string)
    print(result)