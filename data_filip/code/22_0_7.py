import sys
import re

def compress_string(input_string):
    if not input_string:
        return ""
    
    compressed = []
    length = len(input_string)
    current_char = input_string[0]
    count = 1
    
    for i in range(1, length):
        if input_string[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = input_string[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

if __name__ == "__main__":
    sample_input = "aaabbccccddddeee"
    result = compress_string(sample_input)
    print(result)
    sample_input_empty = ""
    result_empty = compress_string(sample_input_empty)
    print(result_empty)
    sample_input_single = "a"
    result_single = compress_string(sample_input_single)
    print(result_single)