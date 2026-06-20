def count_consonants(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = count_consonants(sample_text)
    print(result)