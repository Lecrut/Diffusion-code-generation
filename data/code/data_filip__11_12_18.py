from collections import Counter

def filter_duplicates(s: str) -> str:
    counts = Counter(s)
    result_chars = [char for char in s if counts[char] > 1]
    return "".join(result_chars)

if __name__ == "__main__":
    sample_string = "programming"
    output = filter_duplicates(sample_string)
    print(output)