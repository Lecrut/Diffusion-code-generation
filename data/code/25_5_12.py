import itertools

def run_length_encode(text):
    return [f"{len(list(group))}{char}" for char, group in itertools.groupby(text)]

def run_length_decode(encoded_text):
    result = []
    i = 0
    while i < len(encoded_text):
        count_str = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            count_str += encoded_text[i]
            i += 1
        if count_str:
            char = encoded_text[i]
            result.append(char * int(count_str))
        i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aabcccccaaa"
    encoded = run_length_encode(sample_text)
    print(encoded)
    decoded = run_length_decode("".join(encoded))
    print(decoded)