import string

def count_special_characters(text: str) -> tuple:
    special_chars = set(string.punctuation)
    count = 0
    found = False
    for char in text:
        if char in special_chars:
            count += 1
            found = True
    return count, found

if __name__ == '__main__':
    result = count_special_characters("Hello, World!")
    print(result)