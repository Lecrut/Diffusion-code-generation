import sys
def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_input = "Hello, world! This is a test script."
    result = split_words(sample_input)
    print(f"Input: '{sample_input}'")
    print("Output:", result)
    sys.exit(0)