def count_vowels(text):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in 'ETNRSLAO':
            if char in vowels:
                count += 1
        else:
            if char in vowels:
                count += 1
    return count

if __name__ == '__main__':
    samples = [
        "hello",
        "AEIOU",
        "bcdfg",
        "Python is awesome",
        ""
    ]
    for s in samples:
        result = count_vowels(s)
        print(result)