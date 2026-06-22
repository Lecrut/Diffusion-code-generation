def remove_vowels(text: str) -> str:
    vowels = set("aeiouAEIOU")
    return "".join([char for char in text if char not in vowels])

if __name__ == '__main__':
    sample_text = "Hello World"
    result = remove_vowels(sample_text)
    print(result)