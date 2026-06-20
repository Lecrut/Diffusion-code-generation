def transform(s: str) -> str:
    return s.replace(' ', '_')

if __name__ == '__main__':
    print(transform("Hello World"))