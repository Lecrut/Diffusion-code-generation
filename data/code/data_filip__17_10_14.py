import itertools

def rle_encode(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    
    for char, group in itertools.groupby(input_string):
        length = sum(1 for _ in group)
        if length > 3:
            encoded_parts.append(f"{length}{char}")
        else:
            encoded_parts.append(char * length)
            
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = rle_encode(sample_input)
    print(result)