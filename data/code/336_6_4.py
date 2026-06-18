import sys
def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    sample_input = "abcdef" if False else "aabbcc"
    result = is_unique(sample_input)
    print("Unique:", result)