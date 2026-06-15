import re
def extract_words(text: str) -> list[str]:
    if not text:
        return []
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    sample1 = "Hello world, this is a test."
    sample2 = ""
    sample3 = ".,!?;: and ---"
    sample4 = "Python programming is fun"
    sample5 = "   "
    sample6 = "Onlywords"
    print(f"Sample 1: {extract_words(sample1)}")
    print(f"Sample 2: {extract_words(sample2)}")
    print(f"Sample 3: {extract_words(sample3)}")
    print(f"Sample 4: {extract_words(sample4)}")
    print(f"Sample 5: {extract_words(sample5)}")
    print(f"Sample 6: {extract_words(sample6)}")