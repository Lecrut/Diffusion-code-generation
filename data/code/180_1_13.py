def find_substring(text, target):
    words = set(text.split())
    return target in words

if __name__ == '__main__':
    sample_text = "This is a sample text for testing the substring search functionality."
    target_substring = "sample"
    print(find_substring(sample_text, target_substring))