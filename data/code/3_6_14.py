def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(filter(lambda char: char not in vowels, text))

if __name__ == "__main__":
    sample_input = "Hello World"
    result = remove_vowels(sample_input)
    print(result)