def split_sentence(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world this is an example string for testing"
    result = split_sentence(sample_text)
    print(result)