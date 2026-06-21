import itertools

def run_length_encode(text):
    encoded = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        encoded.append(str(count) + char)
    return ''.join(encoded)

if __name__ == '__main__':
    sample_text = "AAABBBCCDAA"
    result = run_length_encode(sample_text)
    print(result)