from itertools import groupby

def run_length_encode(data):
    if not data:
        return tuple()
    return tuple((len(list(group)), key) for key, group in groupby(data))

if __name__ == '__main__':
    sample1 = "AAABBBCCDAA"
    sample2 = [1, 1, 2, 3, 3, 3, 4, 5, 5]
    sample3 = ""
    sample4 = "XYZ"

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))