import io
import sys

def decode_rle(compressed_string):
    result = io.StringIO()
    length = len(compressed_string)
    i = 0
    
    while i < length:
        if not compressed_string[i].isdigit():
            result.write(compressed_string[i])
            i += 1
            continue
        
        num_start = i
        while i < length and compressed_string[i].isdigit():
            i += 1
        count = int(compressed_string[num_start:i])
        
        if i < length:
            char = compressed_string[i]
            result.write(char * count)
            i += 1
    
    return result.getvalue()

if __name__ == '__main__':
    sample_input = "3a4b2c1d5e"
    decoded_output = decode_rle(sample_input)
    print(decoded_output)
    
    large_sample = "100z"
    large_output = decode_rle(large_sample)
    print(large_output[:20] + "..." if len(large_output) > 20 else large_output)