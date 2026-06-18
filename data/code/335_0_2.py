import sys
def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_input = "Hello world this is a test script"
    result = split_words(sample_input)
    if not isinstance(result, list):
        print("Error: Result must be a list.")
        sys.exit(1)
    for word in result:
        print(word)
    sys.exit(0)