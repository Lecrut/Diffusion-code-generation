def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(filter(lambda c: c not in vowels, text))

if __name__ == '__main__':
    sample_string = "Hello World"
    result = remove_vowels(sample_string)
    print(result)