def trim_string(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample = "   Hello, World!   "
    result = trim_string(sample)
    print(result)