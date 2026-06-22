from itertools import groupby

def compress_run_length(s):
    return ''.join(f"{sum(1 for _ in g)}{k}" for k, g in groupby(s))

if __name__ == '__main__':
    sample = "aaabbcdddeeffffg"
    print(compress_run_length(sample))