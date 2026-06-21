def count_vowels(text):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    result = count_vowels("Hello World")
    print(result)