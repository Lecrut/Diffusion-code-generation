def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join(filter(lambda c: c not in vowels, s))

if __name__ == "__main__":
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)