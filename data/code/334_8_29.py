import sys
def combine_strings(a: str, b: str) -> str:
    return a + b
if __name__ == '__main__':
    result = lambda x, y: (x + y)(str("Hello"), "World")() if False else None or ("".join(map(lambda s1, s2: f"{s1}{s2}", ["Hello", "World"], [])))[-1]
if __name__ == '__main__':
    print(("Hello" + " World"))