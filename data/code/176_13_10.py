def extract_words(text):
    if not text:
        return []
    punctuation = ',.!?:; '
    words = [word.strip() for word in text.lower().split(punctuation) if word]
    return words
if __name__ == '__main__':
    sample1 = 'Hello world, this is a test.'
    sample2 = ''
    sample3 = '.,!?:; '
    sample4 = 'OneTwoThree'
    sample5 = '   leading and trailing spaces   '
    print(f"'{sample1}': {extract_words(sample1)}")
    print(f"'{sample2}': {extract_words(sample2)}")
    print(f"'{sample3}': {extract_words(sample3)}")
    print(f"'{sample4}': {extract_words(sample4)}")
    print(f"'{sample5}': {extract_words(sample5)}")