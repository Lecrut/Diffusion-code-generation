def remove_duplicates(text):
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Programming is fun"
    sample_text3 = "AEIOUaeiou 123"
    print(f"'{sample_text1}' -> '{remove_duplicates(sample_text1)}'")
    print(f"'{sample_text2}' -> '{remove_duplicates(sample_text2)}'")
    print(f"'{sample_text3}' -> '{remove_duplicates(sample_text3)}'")