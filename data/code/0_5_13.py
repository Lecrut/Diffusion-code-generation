def extract_digits(s):
    result = []
    for char in s:
        if char.isdigit():
            result.append(int(char))
    return result

if __name__ == '__main__':
    sample_strings = [
        "a1b2c3",
        "hello world",
        "unicode: ①②③",
        "mixed: 5x7y9z",
        "no digits here!",
        "007 secret agent"
    ]

    for sample in sample_strings:
        digits = extract_digits(sample)
        print(f"{sample!r} -> {digits}")