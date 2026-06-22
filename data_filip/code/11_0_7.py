from collections import Counter

def get_repeated_characters(s: str) -> list:
    counts = Counter(s)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    test_string = "programming"
    result = get_repeated_characters(test_string)
    print(result)