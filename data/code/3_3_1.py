def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    result = []
    for char in text:
        if char not in vowels:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_string = "Hello, World! This is an Example."
    print(remove_vowels(sample_string))