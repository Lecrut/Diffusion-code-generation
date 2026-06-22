def normalize_text(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    result = normalize_text("  hello world  ")
    print(result)