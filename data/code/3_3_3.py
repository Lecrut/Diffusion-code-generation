def remove_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []
    for char in s:
        if char not in vowels:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a Python example."
    output = remove_vowels(sample_string)
    print(output)