from itertools import groupby

def run_length_encode(s):
    return ''.join(f"{len(list(group))}{char}" for char, group in groupby(s))

if __name__ == '__main__':
    sample_string = "AAABBBCCD"
    result = run_length_encode(sample_string)
    print(result)