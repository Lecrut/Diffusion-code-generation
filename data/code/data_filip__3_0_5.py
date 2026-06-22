def remove_vowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in s if char not in vowels])

if __name__ == '__main__':
    sample_string = "Hello World"
    result = remove_vowels(sample_string)
    print(result)