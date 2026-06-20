def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    result = "".join(filter(lambda char: char not in vowels, text))
    return result

if __name__ == '__main__':
    sample_text = "Hello World"
    output = remove_vowels(sample_text)
    print(output)