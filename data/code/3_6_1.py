def remove_vowels(s):
    return ''.join(filter(lambda c: c.lower() not in 'aeiou', s))

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "AEIOU",
        "bcdfg",
        "OpenAI"
    ]
    for s in sample_strings:
        print(remove_vowels(s))