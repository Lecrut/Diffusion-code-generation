import itertools

def run_length_encode(data: str) -> str:
    encoded = []
    for char, group in itertools.groupby(data):
        count = len(list(group))
        encoded.append(f"{char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "wwwwaaadexxxxxx"
    result = run_length_encode(sample_string)
    print(result)