import re
import functools
import operator

def rle_encode(data):
    def chunks():
        it = iter(data)
        current_char = next(it)
        current_count = 1
        for char in it:
            if char == current_char:
                current_count += 1
            else:
                yield (current_char, current_count)
                current_char = char
                current_count = 1
        yield (current_char, current_count)
    
    return [(char, count) for char, count in chunks()]

def rle_decode(encoded_data):
    return list(map(lambda x: x[0] * x[1], encoded_data))

def flatten_pairs(pairs):
    return ''.join(map(lambda p: p[0] * p[1], pairs))

def rle_decode_string(encoded_pairs):
    return flatten_pairs(encoded_pairs)

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    encoded = rle_encode(sample_string)
    print(encoded)
    
    decoded_pairs = rle_decode(encoded)
    print(decoded_pairs)
    
    decoded_string = rle_decode_string(encoded)
    print(decoded_string)
    
    verification = sample_string == decoded_string
    print(verification)
    
    sample_string_2 = "XYZXYZXYZ"
    encoded_2 = rle_encode(sample_string_2)
    print(encoded_2)
    
    decoded_string_2 = rle_decode_string(encoded_2)
    print(decoded_string_2)