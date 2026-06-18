import sys
def check_unique_chars(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    sample_strings = ["hello", "abcdefg"]
    for s in sample_strings:
        result = check_unique_chars(s)
        print(f"{s}: {result}")