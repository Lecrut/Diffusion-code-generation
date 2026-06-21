import itertools

def compress_string(data):
    if not data:
        return ""
    
    def encode_segment(char, group_len):
        if group_len == 1:
            return char
        return str(group_len) + char
    
    grouped = itertools.groupby(data)
    encoded_parts = [
        encode_segment(char, len(list(items)))
        for char, items in grouped
    ]
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    samples = ["", "a", "aaabbc", "abcde", "xxxx", "ab"]
    for sample in samples:
        print(compress_string(sample))