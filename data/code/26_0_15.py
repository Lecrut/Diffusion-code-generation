from itertools import groupby

def run_length_encode(s):
    result = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        result.append((char, count))
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    encoded = run_length_encode(sample_string)
    print(encoded)