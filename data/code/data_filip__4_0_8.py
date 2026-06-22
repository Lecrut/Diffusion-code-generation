def count_consonants(text: str) -> int:
    consonants = set("bcdfghjklmnpqrstvwxyz")
    count = 0
    for char in text:
        if char.lower() in consonants:
            count += 1
    return count

if __name__ == '__main__':
    text = "Hello World!"
    result = count_consonants(text)
    print(result)