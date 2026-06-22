def extract_first_word(text):
    text = text.strip()
    if not text:
        return ""
    words = text.split()
    if words:
        return words[0]
    return ""

if __name__ == '__main__':
    print(extract_first_word("Hello world"))
    print(extract_first_word("   leading spaces and multiple words"))
    print(extract_first_word(""))
    print(extract_first_word("singleword"))
    print(extract_first_word("  "))