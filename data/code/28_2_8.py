from itertools import groupby

def run_length_encode(data: str) -> str:
    return "".join(f"{count}{char}" for char, group in groupby(data) for count in [len(list(group))])

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = run_length_encode(sample_string)
    print(result)