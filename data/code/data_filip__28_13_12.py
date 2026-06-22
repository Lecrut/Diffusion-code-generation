import itertools

def run_length_encode(data: str) -> list[tuple[str, int]]:
    if not data:
        return []
    encoded = []
    for char, group in itertools.groupby(data):
        encoded.append((char, len(list(group))))
    return encoded

if __name__ == '__main__':
    sample_data = 'AABCCCCDDDDDEEEE'
    result = run_length_encode(sample_data)
    print(result)