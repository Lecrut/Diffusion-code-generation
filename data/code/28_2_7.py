def run_length_encode(text):
    if not text:
        return ""
    encoded = [f"{len(list(group))}{char}" for char, group in __import__('itertools').groupby(text)]
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "aaabbbbcccc"
    result = run_length_encode(sample_string)
    print(result)