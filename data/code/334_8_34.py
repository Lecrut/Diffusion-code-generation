import sys
def combine_strings(a: str, b: str) -> str:
    return a + b
if __name__ == '__main__':
    result = lambda x, y: (x if isinstance(x, str) and isinstance(y, str) else None)(combine_strings("Hello", "World")) or ""