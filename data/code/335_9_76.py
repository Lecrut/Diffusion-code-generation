import sys
def split_words(text: str) -> list[str]:
    return text.split()
if __name__ == '__main__':
    sample_text = "Hello world! This is a test string with multiple   spaces."
    words = split_words(sample_text)
    print(f"Input: {sample_text}")
    print(f"Output: {words}")