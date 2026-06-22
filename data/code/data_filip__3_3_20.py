def remove_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join(char for char in s if char not in vowels)

if __name__ == '__main__':
    sample = "Hello World"
    print(remove_vowels(sample))