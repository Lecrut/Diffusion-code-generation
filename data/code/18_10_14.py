import itertools

def run_length_encode(text: str) -> list[tuple[str, int]]:
    return [(char, sum(1 for _ in group)) for char, group in itertools.groupby(text)]

if __name__ == '__main__':
    sample_input = "aabcccccaaa"
    result = run_length_encode(sample_input)
    print(result)