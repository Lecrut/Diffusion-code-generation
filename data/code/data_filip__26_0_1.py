from itertools import groupby

def run_length_encode(text):
    if not text:
        return []
    encoded = []
    for key, group in groupby(text):
        count = len(list(group))
        encoded.append((count, key))
    return encoded

if __name__ == '__main__':
    sample_data = "aaabbccccd"
    result = run_length_encode(sample_data)
    print(result)