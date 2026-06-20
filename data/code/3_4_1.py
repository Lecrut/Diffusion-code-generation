def delete_vowels(text):
    vowels = set("aeiouAEIOU")
    return "".join(char for char in text if char not in vowels)

if __name__ == '__main__':
    result = delete_vowels("Hello World")
    print(result)