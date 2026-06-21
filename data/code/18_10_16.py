from itertools import groupby

def run_length_encode(text: str) -> list:
    if not text:
        return []
    return [(char, sum(1 for _ in group)) for char, group in groupby(text)]

if __name__ == '__main__':
    input_string = "aabbbcccc"
    result = run_length_encode(input_string)
    print(result)