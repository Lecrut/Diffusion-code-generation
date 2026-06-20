def strip_vowels(text: str) -> str:
    vowels = "aeiouAEIOU"
    table = str.maketrans("", "", vowels)
    return text.translate(table)

if __name__ == '__main__':
    print(strip_vowels("Hello World!"))