from itertools import groupby

def run_length_encode(data):
    return ''.join(f"{char}{sum(1 for _ in group) if len(list(group)) > 1 else ''}" for char, group in groupby(data))

def run_length_decode(encoded_data):
    if not encoded_data:
        return ""
    result = []
    i = 0
    while i < len(encoded_data):
        char = encoded_data[i]
        i += 1
        num_str = ""
        while i < len(encoded_data) and encoded_data[i].isdigit():
            num_str += encoded_data[i]
            i += 1
        count = int(num_str) if num_str else 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBCDDDEEEEE"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(f"Original: {sample_input}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")