def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + input_string[i - 1])
            count = 1
    encoded.append(str(count) + input_string[-1])
    return "".join(encoded)

def run_length_decode(encoded_string):
    if not encoded_string:
        return ""
    decoded = []
    i = 0
    while i < len(encoded_string):
        count_str = ""
        while i < len(encoded_string) and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        if i < len(encoded_string):
            count = int(count_str)
            char = encoded_string[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == "__main__":
    sample = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = run_length_encode(sample)
    decoded = run_length_decode(encoded)
    print(sample == decoded)