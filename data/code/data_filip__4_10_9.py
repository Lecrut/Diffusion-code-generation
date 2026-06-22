def count_consonants(text):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "AEIOU"
    sample3 = "bcdfg"
    sample4 = "Python3.9"
    print(count_consonants(sample1))
    print(count_consonants(sample2))
    print(count_consonants(sample3))
    print(count_consonants(sample4))