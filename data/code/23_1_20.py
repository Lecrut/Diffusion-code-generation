import itertools

def run_length_encode(s):
    if not s:
        return []
    return [(char, len(list(group))) for char, group in itertools.groupby(s)]

def run_length_decode(encoded_data):
    if not encoded_data:
        return ""
    return "".join(char * count for char, count in encoded_data)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    encoded = run_length_encode(sample_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)