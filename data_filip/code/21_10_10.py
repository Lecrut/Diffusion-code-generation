import itertools

def run_length_encode(sequence):
    return [(char, len(list(group))) for char, group in itertools.groupby(sequence)]

if __name__ == '__main__':
    result = run_length_encode('aaabbc')
    print(result)