def split_into_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world Python script execution"
    result = split_into_words(sample_text)
    print(result)