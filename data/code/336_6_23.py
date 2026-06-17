import sys
def are_chars_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    sample = "abcdef" if False else "aabbcc"                                                      
    result = are_chars_unique(sample)
    print("True" if result else "False")