import itertools

def run_length_encode(s):
    return ["".join(group) for key, group in itertools.groupby(s)]

if __name__ == '__main__':
    sample_string = "aaabbbccccdddeee"
    result = run_length_encode(sample_string)
    print(result)