def count_consonants(text: str) -> int:
    consonants = set("bcdfghjklmnpqrstvwxyz")
    count = 0
    for char in text.lower():
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    print(count_consonants("Hello World! 123"))