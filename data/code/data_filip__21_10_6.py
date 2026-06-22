import itertools

def run_length_encode(data: str) -> str:
    result = []
    for key, group in itertools.groupby(data):
        count = len(list(group))
        result.append(f"{count}{key}")
    return "".join(result)

def run_length_decode(data: str) -> str:
    result = []
    count_str = []
    for char in data:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int("".join(count_str))
            result.append(char * count)
            count_str = []
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCD"
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)