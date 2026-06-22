from itertools import groupby

def run_length_encode(s):
    return [(k, len(list(g))) for k, g in groupby(s)]

if __name__ == '__main__':
    print(run_length_encode('aabcccccaaa'))