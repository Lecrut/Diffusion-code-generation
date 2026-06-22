import itertools

def run_length_encode(data):
    return ((k, len(list(group))) for k, group in itertools.groupby(data))

def run_length_decode(encoded_data):
    return (char for char, count in encoded_data for _ in range(count))

def encode_to_string(data):
    return "".join(f"{char}{count}" if count > 1 else char for char, count in run_length_encode(data))

def decode_from_string(encoded):
    result = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        count = int(num_str) if num_str else 1
        result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_result = list(run_length_encode(sample_string))
    print(f"Encoded list: {encoded_result}")
    decoded_gen = run_length_decode(encoded_result)
    decoded_string = "".join(decoded_gen)
    print(f"Decoded string: {decoded_string}")
    print(f"Encoded string format: {encode_to_string(sample_string)}")
    print(f"Decoded from string format: {decode_from_string(encode_to_string(sample_string))}")