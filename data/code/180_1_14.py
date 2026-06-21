def find_substring(text, target):
    words = set(text.split())
    return target in words

if __name__ == '__main__':
    text = "This is a sample text for testing the substring search functionality."
    target = "sample"
    print(find_substring(text, target))