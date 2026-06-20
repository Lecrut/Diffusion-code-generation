def eliminate_vowels(text):
    vowels = set("aeiouAEIOU")
    return "".join(filter(lambda char: char not in vowels, text))

if __name__ == '__main__':
    result = eliminate_vowels("Hello World")
    print(result)