def filter_vowels(text: str) -> str:
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in text if char not in vowels)

if __name__ == '__main__':
    result = filter_vowels('Hello World')
    print(result)