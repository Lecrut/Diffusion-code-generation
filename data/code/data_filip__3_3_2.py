def remove_vowels(s):
    vowels = set('aeiouAEIOU')
    result = []
    for char in s:
        if char not in vowels:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    print(remove_vowels('Hello World'))
    print(remove_vowels('Python Programming'))
    print(remove_vowels('AEIOU aeiou'))
    print(remove_vowels(''))
    print(remove_vowels('bcdfg'))