def count_vowels(text):
    if not isinstance(text, str):
        return 0
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    print(count_vowels("Hello World"))
    print(count_vowels(""))
    print(count_vowels("123456"))
    print(count_vowels("rhythm"))