def remove_vowels(text):
    if not text:
        return ""
    vowels = "aeiouAEIOU"
    translator = str.maketrans("", "", vowels)
    return text.translate(translator)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)