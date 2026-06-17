def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_string = "Hello World Python Programming"
    result = split_words(sample_string)
    print(result)