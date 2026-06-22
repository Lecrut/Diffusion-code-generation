from itertools import groupby

def run_length_encode(s):
    return ''.join(str(len(list(group))) + key for key, group in groupby(s))

if __name__ == '__main__':
    sample_strings = [
        "aaaabbbcc",
        "aabbbcccc",
        "abc",
        "a",
        ""
    ]
    for s in sample_strings:
        print(run_length_encode(s))