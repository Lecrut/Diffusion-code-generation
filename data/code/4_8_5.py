def count_consonants(text):
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = 0
    for char in text:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    text = "Hello, World!"
    result = count_consonants(text)
    print(result)