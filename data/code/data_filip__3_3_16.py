def remove_vowels(s):
    vowels = set("aeiouAEIOU")
    return ''.join(char for char in s if char not in vowels)

if __name__ == '__main__':
    print(remove_vowels("Hello World"))