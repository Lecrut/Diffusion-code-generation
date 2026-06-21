def extract_words(text: str) -> list[str]:
    if not text:
        return []
    
    words = text.split()
    cleaned_words = [word.strip(",.!?:; ") for word in words]
    lowercased_words = [word.lower() for word in cleaned_words]
    return lowercased_words

if __name__ == '__main__':
    sample1 = "Hello world, this is a test."
    sample2 = ""
    sample3 = ".,!?:; "
    sample4 = "OneTwoThree"
    sample5 = "   leading and trailing spaces   "
    sample6 = "Word1, Word2;Word3"
    
    print(f"'{sample1}': {extract_words(sample1)}")
    print(f"'{sample2}': {extract_words(sample2)}")
    print(f"'{sample3}': {extract_words(sample3)}")
    print(f"'{sample4}': {extract_words(sample4)}")
    print(f"'{sample5}': {extract_words(sample5)}")
    print(f"'{sample6}': {extract_words(sample6)}")