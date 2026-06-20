def remove_vowels(text: str) -> str:
    vowels = "aeiouAEIOU"
    translator = str.maketrans({char: None for char in vowels})
    return text.translate(translator)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)