from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    return [(key, len(list(group))) for key, group in groupby(data)]

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAAA"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)