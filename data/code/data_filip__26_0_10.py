import itertools

def run_length_encode(s):
    if not s:
        return []
    result = []
    for char, group in itertools.groupby(s):
        count = len(list(group))
        result.append((count, char))
    return result

if __name__ == '__main__':
    sample_string = "aaabbccccdd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)