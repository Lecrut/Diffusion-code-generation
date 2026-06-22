import itertools

def run_length_encode(s):
    return ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))

if __name__ == '__main__':
    sample_strings = ['AABBBCC', 'AAAAA', 'ABABAB', 'XYZXYZXYZ']
    for s in sample_strings:
        print(run_length_encode(s))