def remove_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join(char for char in s if char not in vowels)

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)