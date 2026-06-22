def count_consonants(text):
    if not text:
        return 0
    vowels = set('aeiouAEIOU')
    consonants = set()
    for char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonants.add(char)
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_consonants(sample_text)
    print(result)