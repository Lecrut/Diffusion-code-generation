def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_input = "Hello World This is Python Script"
    result = split_words(sample_input)
    print(result)