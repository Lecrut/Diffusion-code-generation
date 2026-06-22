def capitalize_words(s: str) -> str:
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample = "hello WORLD today is a BEAUTIFUL day"
    result = capitalize_words(sample)
    print(result)