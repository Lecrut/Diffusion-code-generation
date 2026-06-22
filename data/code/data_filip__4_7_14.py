def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in text.lower():
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    result = count_consonants("Hello World")
    print(result)