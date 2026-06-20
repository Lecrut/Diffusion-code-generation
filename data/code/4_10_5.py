def count_consonants(text):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "AEIOU",
        "bcdfg",
        "12345!@#$%",
        "",
        "aEiOuBCDFG",
        "Rhythm",
        "Fly",
        "Queue"
    ]
    for s in sample_strings:
        result = count_consonants(s)
        print(f"String: '{s}' -> Consonants: {result}")