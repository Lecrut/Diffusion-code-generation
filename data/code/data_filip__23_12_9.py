from itertools import groupby

def run_length_encode(s):
    return [(len(list(group)), char) for char, group in groupby(s)]

if __name__ == '__main__':
    print(run_length_encode("AAABBBCCD"))
    print(run_length_encode("ABC"))
    print(run_length_encode(""))
    print(run_length_encode("A"))
    print(run_length_encode("AAAAAA"))