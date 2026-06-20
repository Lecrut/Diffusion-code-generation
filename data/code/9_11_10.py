def trim_string(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    result = trim_string("  hello world  ")
    print(result)