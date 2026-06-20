def capitalize_first(text):
    if not text:
        return text
    first_char = text[0]
    if 'a' <= first_char <= 'z':
        offset = ord('a') - ord('A')
        capitalized = chr(ord(first_char) - offset)
    else:
        capitalized = first_char
    remaining = text[1:]
    return capitalized + remaining

if __name__ == '__main__':
    test_values = ["python", "123start", "", "Zebra", "mixedCase", "a"]
    for value in test_values:
        output = capitalize_first(value)
        print(output)