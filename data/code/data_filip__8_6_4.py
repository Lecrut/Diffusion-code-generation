def split_and_strip(text: str) -> list[str]:
    return [s.strip() for s in text.split(',') if s.strip()]

if __name__ == '__main__':
    result = split_and_strip("  hello , world ,  , foo ")
    print(result)