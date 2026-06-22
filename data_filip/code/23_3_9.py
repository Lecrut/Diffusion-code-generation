import itertools

def run_length_encode(text):
    if not text:
        return ""
    encoded_parts = []
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        encoded_parts.append(f"{char}{count}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_text = "aaabbccccdd"
    result = run_length_encode(sample_text)
    print(result)