def count_consonants(s):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = 0
    for char in s:
        if char in consonants:
            count += 1
    return count

if __name__ == '__main__':
    text = "Hello World"
    result = count_consonants(text)
    print(result)