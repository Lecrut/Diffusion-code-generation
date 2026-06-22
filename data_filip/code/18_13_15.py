import itertools

def run_length_encode(data):
    return ((char, len(list(group))) for char, group in itertools.groupby(data))

def run_length_decode(encoded_data):
    return (char * count for char, count in encoded_data)

def encode_to_string(data):
    return ''.join(f'{char}{count}' for char, count in run_length_encode(data))

def decode_from_string(encoded_str):
    result = []
    i = 0
    while i < len(encoded_str):
        char = encoded_str[i]
        i += 1
        count_str = []
        while i < len(encoded_str) and encoded_str[i].isdigit():
            count_str.append(encoded_str[i])
            i += 1
        count = int(''.join(count_str))
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWWB"
    encoded_str = encode_to_string(sample_input)
    print(encoded_str)
    decoded_str = decode_from_string(encoded_str)
    print(decoded_str)