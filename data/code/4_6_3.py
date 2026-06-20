def count_consonants(text: str) -> int:
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = 0
    for char in text:
        if char.isalpha() and char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World! This is a test string with some consonants."
    result = count_consonants(sample_text)
    print(result)