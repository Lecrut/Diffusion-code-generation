from collections import Counter

def find_chars_appearing_twice(s: str) -> list:
    counts = Counter(s)
    result = [char for char, count in counts.items() if count == 2]
    return sorted(result)

if __name__ == '__main__':
    sample_string = "aabbccdddeeffg"
    result = find_chars_appearing_twice(sample_string)
    print(result)