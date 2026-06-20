def trim_spaces(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample = "   Hello World   "
    print(trim_spaces(sample))