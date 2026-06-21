import itertools

def compress_string(s: str) -> str:
    if not s:
        return ""
    
    result = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        result.append(f"{count}{key}")
    
    return "".join(result)

if __name__ == '__main__':
    sample = "aaabbcccc"
    output = compress_string(sample)
    print(output)