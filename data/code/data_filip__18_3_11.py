from itertools import groupby

def run_length_encode(s: str) -> str:
    return ''.join(f'{len(list(g))}{k}' for k, g in groupby(s))

if __name__ == '__main__':
    print(run_length_encode("aaabbccccd"))