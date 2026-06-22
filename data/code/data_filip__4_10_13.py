def count_consonants(text):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample1 = "Hello World"
    print(count_consonants(sample1))
    sample2 = "Python Programming"
    print(count_consonants(sample2))
    sample3 = "aeiou"
    print(count_consonants(sample3))
    sample4 = "BCDFG"
    print(count_consonants(sample4))
    sample5 = "12345!@#"
    print(count_consonants(sample5))