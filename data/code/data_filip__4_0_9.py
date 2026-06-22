def count_consonants(text):
    vowels = set('aeiou')
    count = 0
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char not in vowels:
                count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result = count_consonants(sample_string)
    print(result)