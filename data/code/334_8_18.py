import sys
def combine_strings(s1: str, s2: str) -> str:
    return f"{s1}{s2}"
if __name__ == '__main__':
    result = lambda x, y: (x + y)(lambda a, b: print(a+b))("Hello", "World") if False else None or combine_strings("Hi", "!"); sys.exit(0)