import itertools

def encode_text(text):
    if not text:
        return ""
    encoded_parts = []
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        encoded_parts.append(f"{char}{count}")
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = encode_text(sample_input)
    print(result)