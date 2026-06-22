def remove_vowels(text: str) -> str:
    return "".join(filter(lambda c: c.lower() not in "aeiou", text))

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)