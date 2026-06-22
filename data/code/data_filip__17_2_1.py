import itertools

def run_length_encode(text: str) -> str:
    if not text:
        return ''
    compressed_parts = []
    for char, group in itertools.groupby(text):
        count = len(list(group))
        compressed_parts.append(f"{count}{char}")
    return ''.join(compressed_parts)

if __name__ == '__main__':
    sample_string = "aaabbbcccd"
    result = run_length_encode(sample_string)
    print(result)