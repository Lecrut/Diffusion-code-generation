def split_sentence(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample = "Hello world this is Python"
    result = split_sentence(sample)
    print(result)