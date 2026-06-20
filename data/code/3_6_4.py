def remove_vowels(text):
    return "".join(filter(lambda char: char not in "aeiouAEIOU", text))

if __name__ == "__main__":
    sample_text = "Hello World from Python"
    result = remove_vowels(sample_text)
    print(result)