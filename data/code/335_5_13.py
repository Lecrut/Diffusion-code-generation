import sys
def split_words(input_str: str) -> list[str]:
    return input_str.split()
if __name__ == '__main__':
    sample_input = "Hello world, this is a test sentence."
    result = split_words(sample_input)
    print(" ".join(result))