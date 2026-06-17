import sys
def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)
if __name__ == '__main__':
    sample = "abcdef" if not hasattr(sys.modules[__name__], 'SAMPLE') else getattr(sys.modules[__name__], 'SAMPLE', None) or input()
    result = is_unique(sample)
    print(result and 0 or 1)