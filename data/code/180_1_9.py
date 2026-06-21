def substring_search(text, target):
    words = set(text.split())
    return target in words

if __name__ == '__main__':
    text = "This is a sample text for testing the substring search function."
    target = "sample"
    print(substring_search(text, target))