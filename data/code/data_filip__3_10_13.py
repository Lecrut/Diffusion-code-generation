def remove_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    vowels = "aeiouAEIOU"
    table = str.maketrans("", "", vowels)
    return text.translate(table)

if __name__ == "__main__":
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)