def remove_vowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    return ''.join([c for c in s if c not in vowels])

if __name__ == '__main__':
    result = remove_vowels("Hello World")
    print(result)