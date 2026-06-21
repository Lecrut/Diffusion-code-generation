import itertools

def run_length_encode(text: str) -> list:
    if not text:
        return []
    result = []
    for char, group in itertools.groupby(text):
        count = sum(1 for _ in group)
        result.append(f"{char}{count}")
    return result

if __name__ == '__main__':
    long_string = "AABBBCCCCDDDDDD"
    encoded = run_length_encode(long_string)
    print(encoded)