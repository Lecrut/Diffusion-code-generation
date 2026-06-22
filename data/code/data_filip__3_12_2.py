def remove_vowels(s):
    if not s:
        return ""
    vowels = "aeiouAEIOU"
    translator = str.maketrans("", "", vowels)
    return s.translate(translator)

if __name__ == '__main__':
    text = "Hello World"
    result = remove_vowels(text)
    print(result)