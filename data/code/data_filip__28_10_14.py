from itertools import groupby

def run_length_encode(data):
    return tuple((k, len(list(g))) for k, g in groupby(data))

if __name__ == '__main__':
    sample_data = 'aaabbcdeeee'
    result = run_length_encode(sample_data)
    print(result)