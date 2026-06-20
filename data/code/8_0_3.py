def split_commas(text: str) -> list:
    parts = text.split(',')
    return [p for p in parts if p]

if __name__ == '__main__':
    print(split_commas("a, b,,c,d, "))
    print(split_commas(""))
    print(split_commas("hello"))
    print(split_commas(", , ,"))