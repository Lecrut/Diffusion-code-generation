import itertools

def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    for char, group in itertools.groupby(text):
        length = len(list(group))
        encoded.append(f"{char}{length}")
    return "".join(encoded)

if __name__ == '__main__':
    result = run_length_encode("aabcccccaaa")
    print(result)