def strip_text(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample = "  hello world  "
    print(strip_text(sample))