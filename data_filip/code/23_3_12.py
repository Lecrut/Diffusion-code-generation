from itertools import groupby

def run_length_encode(text: str) -> str:
    if not text:
        return ""
    
    result = []
    for key, group in groupby(text):
        count = sum(1 for _ in group)
        result.append(f"{count}{key}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbcccc"
    encoded = run_length_encode(sample_text)
    print(encoded)