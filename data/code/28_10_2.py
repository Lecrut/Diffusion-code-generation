from itertools import groupby

def run_length_encode(data):
    result = []
    for key, group in groupby(data):
        count = len(list(group))
        result.append((key, count))
    return tuple(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)